from bottle import *
from model import *
from random import randint
@get("/")
def mainpage():
    user=request.get_cookie("id")
    if(user==None):
        return template("strani/start/intro.tpl")
    else:
        redirect("../access/main_inside")

@get("/login")
def login_page():
    return template("strani/start/login.tpl",string="Vpisite uporabnisko ime in geslo")
    
@post("/login_submit")
def check_password():
    user=request.forms.getunicode("user")
    password=request.forms.getunicode("password")
    print(user+" "+password)
    is_ok=model.check_password(user,password)
    if(is_ok):
        response.set_cookie("id",user,secret='gostilnaprimari')
        redirect("../access/main_inside")
    else:
        return template("strani/start/login.tpl",string="Napacno geslo")

@get("/company_login")
def company_login_page():
    return template("strani/start/company_login.tpl",string="")

@post("/company_login")
def company_login_page():
    podjetje=request.forms.getunicode("podjetje")
    password=request.forms.getunicode("password")
    print(podjetje+" "+password)
    is_admin=model.check_password_company_admin(podjetje,password)
    if(is_admin):
        response.set_cookie("admin","yes",secret='gostilnaprimari')
        response.set_cookie("company",podjetje,secret='gostilnaprimari')
        redirect("../company/main_inside")
    is_ok=model.check_password_company(podjetje,password)
    if(is_ok):
        response.set_cookie("company",podjetje,secret='gostilnaprimari')
        redirect("../company/main_inside")
    else:
        return template("strani/start/company_login.tpl",string="Napacno geslo")

@get("/admin")
def statistika():
    return template("strani/start/statistika.tpl",model=model)

@get("/company/main_inside")
def glavna_stran_podjetje():
    response.delete_cookie("id",path="/")
    company=request.get_cookie("company",secret="gostilnaprimari")
    if(company==None):
        print("Hacker podjetje")
        redirect("/")
    return template("strani/company/main_inside_podjetje.tpl",podjetje=company)

@get("/company/manage_users")
def glavna_stran_podjetje():
    company=request.get_cookie("company",secret="gostilnaprimari")
    return template("strani/company/manage_users.tpl",model=model,podjetje=company)

@get("/company/redirect/<ime>")
def preusmeri(ime):
    response.set_cookie("id",ime,secret='gostilnaprimari',path="/")
    redirect("/access/main_inside")

@get("/company/change_password")
def spremeni_geslo():
    return template("strani/company/spremeni_geslo.tpl",string="")

@post("/company/change_password")
def spremeni_geslo_post():
    podjetje=request.get_cookie("company",secret='gostilnaprimari')
    pod=model.getCompany(podjetje)
    ngeslo=request.forms.getunicode("geslo1")
    ngeslo2=request.forms.getunicode("geslo2")
    if(len(ngeslo<5)):
        return template("strani/company/spremeni_geslo.tpl",string="Geslo je prekratko.")
    if not all(ord(c) < 128 for c in ngeslo):
        return template("strani/company/spremeni_geslo.tpl",string="Geslo vsebuje cudne znake. Morda sumnike.")
    if " " in ngeslo:
         return template("strani/company/spremeni_geslo.tpl",string="Geslo vsebuje presledke")
    if(not ngeslo==ngeslo2):
        return template("strani/company/spremeni_geslo.tpl",string="Gesli nista enaki")
    pod.geslo=model.hash_password(ngeslo)
    model.writeSaveFile()
    redirect("/company/main_inside")

@get("/company/odjava")
def odjava():
    response.delete_cookie("company",path="/")
    redirect("/access/main_inside")

@get("/access/main_inside")
def glavna_stran():
    user=request.get_cookie("id",secret='gostilnaprimari')
    company=request.get_cookie("company",secret="gostilnaprimari")
    if(user==None):
        print("Hacker")
        redirect("/")
    return template("strani/access/glavna_stran.tpl",user=model.getUser(user),company=(company!=None))

@get("/access/narocila")
def narocila():
    user=request.get_cookie("id",secret='gostilnaprimari')
    admin=request.get_cookie("admin",secret="gostilnaprimari")=="yes"
    return template("strani/access/narocila.tpl",user=model.getUser(user),admin=admin)

@post("/access/narocilo/<input>")
def obdelaj_spremembo(input):
    user=model.getUser(request.get_cookie("id",secret='gostilnaprimari'))
    dan=int(input.split(".")[0])
    mesec=int(input.split(".")[1])
    leto=int(input.split(".")[2])
    stevilo=int(input.split(".")[3])
    user.sprememba(datum(dan,mesec,leto),stevilo)
    model.writeSaveFile()
    redirect("/access/narocila")

@get("/access/spremeni_ime")
def spremeni_ime():
    return template("strani/access/spremeni_ime.tpl",string="")
@post("/access/spremeni_ime")
def spremeni_ime_post():
    user1=model.getUser(request.get_cookie("id",secret="gostilnaprimari"))
    nime=request.forms.getunicode("ime")
    for user in model.users:
        if user.ime==nime:
            return template("strani/access/spremeni_ime.tpl",string="Ime je ze uporabljeno.")
    if not all(ord(c) < 128 for c in nime):
        return template("strani/access/spremeni_ime.tpl",string="Ime vsebuje cudne znake. Morda sumnike.")
    if " " in nime:
         return template("strani/access/spremeni_ime.tpl",string="Ime vsebuje presledke")
    response.set_cookie("id",nime,path="/",secret='gostilnaprimari')
    user1.ime=nime
    model.writeSaveFile()
    redirect("/access/main_inside")

@get("/access/spremeni_geslo")
def spremeni_geslo():
    return template("strani/access/spremeni_geslo.tpl",string="")
@post("/access/spremeni_geslo")
def spremeni_geslo_post():
    user=model.getUser(request.get_cookie("id",secret='gostilnaprimari'))
    ngeslo=request.forms.getunicode("geslo1")
    ngeslo2=request.forms.getunicode("geslo2")
    if(len(ngeslo<5)):
        return template("strani/access/spremeni_geslo.tpl",string="Geslo je prekratko.")
    if not all(ord(c) < 128 for c in ngeslo):
        return template("strani/access/spremeni_geslo.tpl",string="Geslo vsebuje cudne znake. Morda sumnike.")
    if " " in ngeslo:
         return template("strani/access/spremeni_geslo.tpl",string="Geslo vsebuje presledke")
    if(not ngeslo==ngeslo2):
        return template("strani/access/spremeni_geslo.tpl",string="Gesli nista enaki")
    user.geslo=model.hash_password(ngeslo)
    model.writeSaveFile()
    redirect("/access/main_inside")

@get("/access/odjava")
def odjava():
    response.delete_cookie("id",path="/")
    redirect("/")

@get("/img/<ime>")
def img(ime):
    print("slika")
    return static_file(ime, root='slike')

model=Model()
run(host='0.0.0.0', port=8080, debug=True, reloader=True)
