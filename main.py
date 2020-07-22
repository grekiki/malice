from bottle import *
from model import *
from random import randint
import smtplib
import _thread
import time
import poplib
import imaplib
import email

@get("/main")
def glavna_stran():
    return template("strani/glavna_stran.tpl")


@get("/img/<ime>")
def img(ime):
    print("slika")
    return static_file(ime, root='slike')

port = os.environ.get('PORT', 5000)
run(host='0.0.0.0', port=port, debug=True, reloader=False)
