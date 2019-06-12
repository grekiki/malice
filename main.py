from bottle import *
from model import *

@get("/")
def mainpage():
    user=request.get_cookie("id")
    if(user==None):
        return template("strani/start/intro.tpl")
    else:
        redirect("../access/main_inside")

@get("/register")
def stran_registracija():
    return template("strani/start/registracija.tpl",string="Vpišite svoje podatke")

@post("/register_submit")
def poskusi_registracijo():
    ime=request.forms.getunicode("user")
    geslo=request.forms.getunicode("password")
    geslo2=request.forms.getunicode("password2")
    podjetje=request.forms.getunicode("podjetje")
    print("Poskus registracije osebe "+ime+" "+geslo+" "+geslo2+" "+podjetje)
    response=model.registriraj(ime,geslo,geslo2,podjetje)
    print(len(model.users))
    if response!="Registracija je uspela":
        return template("strani/start/registracija.tpl",string=response)
    else:
        return template("strani/start/uspesna_registracija") 

@get("/login")
def login_page():
    return template("strani/start/login.tpl",string="Vpišite uporabniško ime in geslo")
    
@post("/login_submit")
def check_password():
    user=request.forms.getunicode("user")
    password=request.forms.getunicode("password")
    print(user+" "+password)
    is_ok=model.check_password(user,password)
    if(is_ok):
        response.set_cookie("id",user)
        redirect("../access/main_inside")
    else:
        return template("strani/start/login.tpl",string="Napačno geslo")

@get("/access/main_inside")
def glavna_stran():
    user=request.get_cookie("id")
    if(user==None):
        print("Hacker")
        redirect("../")
    return template("strani/access/glavna_stran.tpl",user=model.getUser(user))


@get("/access/narocila")
def glavna_stran():
    user=request.get_cookie("id")
    return template("strani/access/narocila.tpl",user=model.getUser(user))

@get("/access/narocilo/<input>")
def obdelaj_spremembo(input):
    user=model.getUser(request.get_cookie("id"))
    dan=int(input.split(".")[0])
    mesec=int(input.split(".")[1])
    leto=int(input.split(".")[2])
    stevilo=int(input.split(".")[3])
    user.sprememba(datum(dan,mesec,leto),stevilo)
    model.writeSaveFile()
    redirect("/access/narocila")

@route('/download/<ime>')
def download(ime):
    return static_file(ime, root="datoteke")

@get("/img/<ime>")
def img(ime):
    print("slika")
    return static_file(ime, root='slike')

model=Model()
run(host='0.0.0.0', port=8080, debug=True, reloader=True)
