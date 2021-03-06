from bottle import *
from model import *
from random import randint
import smtplib
import _thread
import time
import poplib
import imaplib
import email

username = "backupmalice@gmail.com"
password = "q1w2e3r4t51543ad"
secret = "gostilnaPriMari"


def make_backup():
    while(True):
        time.sleep(600)  # 600 ko bo mogoče
        print("Making backup")
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(username, password)
        s = ""
        with open("datoteke/podatki.txt") as file:
            for line in file:
                s += line
            smtpObj.sendmail('backupmalice@gmail.com',
                             'backupmalice@gmail.com', "Subject:podatki.txt\n\n"+s)
            s = ""
            file.close()
        with open("datoteke/podjetja.txt") as file:
            for line in file:
                s += line
            file.close()
        smtpObj.sendmail('backupmalice@gmail.com',
                         'backupmalice@gmail.com', "Subject:podjetja.txt\n\n"+s)
        smtpObj.quit()
        print("Backup complete")


def read_backup():
    print("reading")
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username, password)
    mail.list()
    # nekje sem to našel pa dela :)
    # Out: list of "folders" aka labels in gmail.
    mail.select("inbox")  # connect to inbox.
    # print("lol")
    _, data = mail.search(None, "ALL")
    ids = data[0]  # data is a list.
    id_list = ids.split()
    latest_email_id = id_list[-1]
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            with open("datoteke/podjetja.txt", "w") as file:
                string = body.decode('utf-8').strip()+"\n\n"
                for line in string.split("\n"):
                    file.write(line)
                file.close()

    latest_email_id = id_list[-2]
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            with open("datoteke/podatki.txt", "w") as file:
                string = body.decode('utf-8').strip()+"\n\n"
                for line in string.split("\n"):
                    file.write(line)
                file.close()
    print("Backup read from server. Go to launch. ")


@get("/")
def mainpage():
    user = request.get_cookie("id")
    if(user == None):
        return template("strani/start/intro.tpl")
    else:
        redirect("../access/main_inside")


@get("/login")
def login_page():
    return template("strani/start/login.tpl", string="Vpisite uporabnisko ime in geslo")


@post("/login_submit")
def check_password():
    user = request.forms.getunicode("user")
    password = request.forms.getunicode("password")
    print(user+" "+password)
    is_ok = model.check_password(user, password)
    if(is_ok):
        response.set_cookie("id", user, secret=secret)
        redirect("../access/main_inside")
    else:
        return template("strani/start/login.tpl", string="Napacno geslo")


@get("/company_login")
def company_login_page():
    return template("strani/start/company_login.tpl", string="")


@post("/company_login")
def company_login_page():
    podjetje = request.forms.getunicode("podjetje")
    password = request.forms.getunicode("password")
    print(podjetje+" "+password)
    is_admin = model.check_password_company_admin(podjetje, password)
    if(is_admin):
        response.set_cookie("admin", "yes", secret=secret)
        response.set_cookie("company", podjetje, secret=secret)
        redirect("../company/main_inside")
    is_ok = model.check_password_company(podjetje, password)
    if(is_ok):
        response.set_cookie("company", podjetje, secret=secret)
        redirect("../company/main_inside")
    else:
        return template("strani/start/company_login.tpl", string="Napacno geslo")


@get("/admin")
def statistika():
    ans, arr, cache, dan = model.statistika()
    return template("strani/start/statistika.tpl", model=model, ans=ans, arr=arr, cache=cache, dan=dan)


@get("/company/main_inside")
def glavna_stran_podjetje():
    response.delete_cookie("id", path="/")
    company = request.get_cookie("company", secret=secret)
    if(company == None):
        print("Hacker podjetje")
        redirect("/")
    return template("strani/company/main_inside_podjetje.tpl", podjetje=company)


@get("/company/manage_users")
def glavna_stran_podjetje():
    company = request.get_cookie("company", secret=secret)
    return template("strani/company/manage_users.tpl", model=model, podjetje=company)


@get("/company/redirect/<ime>")
def preusmeri(ime):
    response.set_cookie("id", ime, secret=secret, path="/")
    redirect("/access/main_inside")


@get("/company/change_password")
def spremeni_geslo():
    return template("strani/company/spremeni_geslo.tpl", string="")


@post("/company/change_password")
def spremeni_geslo_post():
    podjetje = request.get_cookie("company", secret=secret)
    pod = model.getCompany(podjetje)
    ngeslo = request.forms.getunicode("geslo1")
    ngeslo2 = request.forms.getunicode("geslo2")
    if(len(ngeslo) < 5):
        return template("strani/company/spremeni_geslo.tpl", string="Geslo je prekratko.")
    if not all(ord(c) < 128 for c in ngeslo):
        return template("strani/company/spremeni_geslo.tpl", string="Geslo vsebuje cudne znake. Morda sumnike.")
    if " " in ngeslo:
        return template("strani/company/spremeni_geslo.tpl", string="Geslo vsebuje presledke")
    if(not ngeslo == ngeslo2):
        return template("strani/company/spremeni_geslo.tpl", string="Gesli nista enaki")
    pod.geslo = model.hash_password(ngeslo)
    model.writeSaveFile()
    redirect("/company/main_inside")


@get("/company/odjava")
def odjava():
    response.delete_cookie("company", path="/")
    redirect("/access/main_inside")


@get("/access/main_inside")
def glavna_stran():
    user = request.get_cookie("id", secret=secret)
    company = request.get_cookie("company", secret=secret)
    if(user == None):
        print("Hacker")
        redirect("/")
    return template("strani/access/glavna_stran.tpl", user=model.getUser(user), company=(company != None))


@get("/access/narocila")
def narocila():
    user = request.get_cookie("id", secret=secret)
    admin = request.get_cookie("admin", secret=secret) == "yes"
    return template("strani/access/narocila.tpl", user=model.getUser(user), admin=admin, model=model)


@post("/access/narocilo/<input>")
def obdelaj_spremembo(input):
    user = model.getUser(request.get_cookie("id", secret=secret))
    dan = int(input.split(".")[0])
    mesec = int(input.split(".")[1])
    leto = int(input.split(".")[2])
    stevilo = int(input.split(".")[3])
    user.sprememba(datum(dan, mesec, leto), stevilo)
    model.writeSaveFile()
    redirect("/access/narocila")


@get("/access/spremeni_ime")
def spremeni_ime():
    return template("strani/access/spremeni_ime.tpl", string="")


@post("/access/spremeni_ime")
def spremeni_ime_post():
    user1 = model.getUser(request.get_cookie("id", secret=secret))
    nime = request.forms.getunicode("ime")
    for user in model.users:
        if user.ime == nime:
            return template("strani/access/spremeni_ime.tpl", string="Ime je ze uporabljeno.")
    if not all(ord(c) < 128 for c in nime):
        return template("strani/access/spremeni_ime.tpl", string="Ime vsebuje cudne znake. Morda sumnike.")
    if " " in nime:
        return template("strani/access/spremeni_ime.tpl", string="Ime vsebuje presledke")
    response.set_cookie("id", nime, path="/", secret=secret)
    user1.ime = nime
    model.writeSaveFile()
    redirect("/access/main_inside")


@get("/access/spremeni_geslo")
def spremeni_geslo():
    return template("strani/access/spremeni_geslo.tpl", string="")


@post("/access/spremeni_geslo")
def spremeni_geslo_post():
    user = model.getUser(request.get_cookie("id", secret=secret))
    ngeslo = request.forms.getunicode("geslo1")
    ngeslo2 = request.forms.getunicode("geslo2")
    if(len(ngeslo) < 5):
        return template("strani/access/spremeni_geslo.tpl", string="Geslo je prekratko.")
    if not all(ord(c) < 128 for c in ngeslo):
        return template("strani/access/spremeni_geslo.tpl", string="Geslo vsebuje cudne znake. Morda sumnike.")
    if " " in ngeslo:
        return template("strani/access/spremeni_geslo.tpl", string="Geslo vsebuje presledke")
    if(not ngeslo == ngeslo2):
        return template("strani/access/spremeni_geslo.tpl", string="Gesli nista enaki")
    user.geslo = model.hash_password(ngeslo)
    model.writeSaveFile()
    redirect("/access/main_inside")


@get("/access/odjava")
def odjava():
    response.delete_cookie("id", path="/")
    redirect("/")


@get("/img/<ime>")
def img(ime):
    print("slika")
    return static_file(ime, root='slike')


print("started")
read_backup()
model = Model()
try:
    thread.start_new_thread(make_backup, ())
except:
    print("Error: unable to start thread")
port = os.environ.get('PORT', 5000)
run(host='0.0.0.0', port=port, debug=True, reloader=False)
