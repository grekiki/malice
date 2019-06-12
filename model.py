from datetime import *
import calendar
import hashlib, binascii, os
class datum:
    def __init__(this,dan,mesec,leto):
        this.dan=dan
        this.mesec=mesec
        this.leto=leto
    def __str__(this):
        return str(this.dan)+"."+str(this.mesec)+"."+str(this.leto)
    def __eq__(this,other):
        return str(this)==str(other)
    def __hash__(this):
        return hash(str(this))
    def cmp(this,other):
        if(this==other):
            return 0
        if(not this.leto==other.leto):
            return this.leto-other.leto
        if(not this.mesec==other.mesec):
            return this.mesec-other.mesec
        if(not this.dan==other.dan):
            return this.dan-other.dan
        print("napaka v primerjanju datumov")
        return 0 
    def __lt__(this,other):
        return this.cmp(other)<0

    def dan_v_tednu_string(this):
        dan = datetime(this.leto,this.mesec,this.dan)
        return ["Ponedeljek","Torek","Sreda","Cetrtek","Petek","Sobota","Nedelja"][dan.weekday()]
    def dan_v_tednu_int(this):
        dan = datetime(this.leto,this.mesec,this.dan)
        return dan.weekday()

class uporabnik:
    def __init__(this,ime,geslo,podjetje,spremembe):
        this.ime=ime
        this.geslo=geslo
        this.podjetje=podjetje
        this.spremembe=spremembe
        this.delta=this.parse(spremembe)
        #print(this.ime+" "+str(this.delta))
    def parse(this,spremembe):
        seznam={}
        oklepaj=-1
        vejica=-1
        zaklepaj=-1
        for i in range(0,len(spremembe)):
            if(spremembe[i]=="("):
                oklepaj=i
            elif(spremembe[i]==","):
                vejica=i
            elif(spremembe[i]==")"):
                zaklepaj=i
                ok=(oklepaj>0 and oklepaj<zaklepaj and oklepaj<vejica and vejica<zaklepaj)
                #print(ok)
                #print(spremembe[1+oklepaj:vejica]+" "+spremembe[1+vejica:zaklepaj])
                ls=spremembe[1+oklepaj:vejica].split(".")
                seznam[datum(int(ls[0]),int(ls[1]),int(ls[2]))]=int(spremembe[1+vejica:zaklepaj])
        #print(seznam)
        return seznam
    def sprememba(this,datum,stevilo):
        this.delta[datum]=stevilo
        if(stevilo==0):
            this.delta.pop[datum]
        #print(this.delta)
        this.updateStr()
    def updateStr(this):
        ans="{"
        #print("update")
        for t in this.delta:
            print(t)
            ans+="("+str(t.dan)+"."+str(t.mesec)+"."+str(t.leto)+","+str(this.delta[t])+"),"
        ans=ans[:-1]
        ans+="}"
        this.spremembe=ans
    def getMenu(this,datum):
        if not datum in this.delta:
            return 0
        else:
            return this.delta[datum]
    def count_previous_month(this):
        count=0
        year=datetime.today().year
        month=datetime.today().month
        if(month==1):
            month=12
            year-=1
        else:
            month-=1
        for day in range(1,32):
            if(this.getMenu(datum(day,month,year))!=0):
                count+=1
        return count
class podjetje:
    def __init__(this,ime,geslo):
        this.ime=ime
        this.geslo=geslo
    
class Model:
    def __init__(this):
        this.readSaveFile()
    def readSaveFile(this):
        #print("read")
        file=open("datoteke/podatki.txt","r")
        this.users=[]
        for line in file:
            #print(line)
            arr=line.split()
            ime=arr[0]
            geslo=arr[1]
            podjetje1=arr[2]
            spremembe=arr[3]
            this.users.append(uporabnik(ime,geslo,podjetje1,spremembe))
        file.close()

        file=open("datoteke/podjetja.txt","r")
        this.podjetja=[]
        for line in file:
            #print(line)
            arr=line.split()
            ime=arr[0]
            geslo=arr[1]
            this.podjetja.append(podjetje(ime,geslo))
        file.close()
    def writeSaveFile(this):
        print("write")
        file=open("datoteke/podatki.txt","w")
        for user in this.users:
            #print(user.ime+" "+user.geslo+" "+user.podjetje+" "+user.spremembe)
            file.write(user.ime+" "+user.geslo+" "+user.podjetje+" "+user.spremembe+"\n")
        file.close()
        file=open("datoteke/podjetja.txt","w")
        for podjetje in this.podjetja:
            #print(user.ime+" "+user.geslo+" "+user.podjetje+" "+user.spremembe)
            file.write(podjetje.ime+" "+podjetje.geslo+"\n")
        file.close()
        this.readSaveFile()
    def check_password(this,username,password):
        for user in this.users:
            if user.ime==username:
                return this.verify_password(user.geslo,password)
        return False
    def check_password_company(this,podjetje,geslo):
        for p in this.podjetja:
            if p.ime==podjetje:
                return this.verify_password(p.geslo,geslo)
        return False
    def registriraj(this,ime,geslo,geslo2,podjetje):
        #print(ime+" "+geslo)
        if " " in ime or " " in geslo or len(ime)==0 or len(geslo)==0:
            return "Ime ali geslo sta prekratka ali vsebujeta presledke"

        if not all(ord(c) < 128 for c in ime):
            return "Ime vsebuje čudne znake. Morda črke č, š,ž ali kaj podobnega."
        if not all(ord(c) < 128 for c in geslo):
            return "Geslo vsebuje čudne znake. Morda črke č, š,ž ali kaj podobnega."
    
        for user in this.users:
            if user.ime==ime:
                return "Ime že obstaja"
        if(geslo!=geslo2):
            return "Gesli nista enaki"
        this.users.append(uporabnik(ime,this.hash_password(geslo),podjetje,"{}"))
        this.writeSaveFile()
        return "Registracija je uspela"
    def getUser(this,ime):
        for user in this.users:
            if user.ime==ime:
                return user
        print("Uporabnika "+ime+" ni mogoče najti")
        return False
    def hash_password(this,password):#https://www.vitoshacademy.com/hashing-passwords-in-python/
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')
    def verify_password(this,stored_password, provided_password):
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                    provided_password.encode('utf-8'), 
                                    salt.encode('ascii'), 
                                    100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password
