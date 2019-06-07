from bottle import *
from model import *

@get("/")
def mainpage():
    user=request.get_cookie("id")
    if(user==None):
        return template("strani/intro.tpl")
    else:
        redirect("../main_inside")

@get("/register")
def stran_registracija():
    return template("strani/registracija.tpl",string="Vpišite svoje podatke")

@post("/register_submit")
def poskusi_registracijo():
    ime=request.forms.getunicode("user")
    geslo=request.forms.getunicode("password")
    geslo2=request.forms.getunicode("password2")
    podjetje=request.forms.getunicode("podjetje")
    print("Poskus registracije osebe "+ime+" "+geslo+" "+geslo2+" "+podjetje)
    ok=model.registriraj(ime,geslo,geslo2,podjetje)
    print(len(model.users))
    if not ok:
        return template("strani/registracija.tpl",string="Registracija ni uspela")
    else:
        return template("strani/uspesna_registracija") 

@get("/login")
def login_page():
    return template("strani/login.tpl",string="Vpišite uporabniško ime in geslo")
    
@post("/login_submit")
def check_password():
    user=request.forms.getunicode("user")
    password=request.forms.getunicode("password")
    is_ok=model.check_password(user,password)
    if(is_ok):
        response.set_cookie("id",user)
        redirect("../main_inside")
    else:
        return template("strani/login.tpl",string="Napačno geslo")

@get("/main_inside")
def glavna_stran():
    user=request.get_cookie("id")
    if(user==None):
        print("Hacker")
        redirect("../")
    return template("strani/glavna_stran.tpl",user=model.getUser(user))

model=Model()
run(host='localhost', port=8080, debug=True, reloader=True)