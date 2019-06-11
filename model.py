from datetime import *
import calendar
class datum:
    def __init__(this,dan,mesec,leto):
        this.dan=dan
        this.mesec=mesec
        this.leto=leto
    def delavni_dan(this):
        dan = datetime.date(this.leto,this.mesec,this.dan)
        if dan.weekday()>=5:
            return False
        file=open("datoteke/prazniki.txt","r")
        for line in file:
            if line==this.dan+"."+this.mesec+"."+this.leto:
                return False
        return True
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
                seznam[(int(ls[0]),int(ls[1]),int(ls[2]))]=int(spremembe[1+vejica:zaklepaj])
        #print(seznam)
        return seznam
    def sprememba(this,datum,stevilo):
        this.delta[datum]=stevilo
        #print(this.delta)
        this.updateStr()
    def updateStr(this):
        ans="{"
        #print("update")
        for t in this.delta:
            #print(t)
            ans+="("+str(t[0])+"."+str(t[1])+"."+str(t[2])+","+str(this.delta[t])+"),"
        ans=ans[:-1]
        ans+="}"
        this.spremembe=ans
    def getMenu(this,datum):
        if not datum in this.delta:
            return 1
        else:
            return this.delta[datum]

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
            podjetje=arr[2]
            spremembe=arr[3]
            this.users.append(uporabnik(ime,geslo,podjetje,spremembe))
        file.close()
    def writeSaveFile(this):
        print("write")
        file=open("datoteke/podatki.txt","w")
        for user in this.users:
            #print(user.ime+" "+user.geslo+" "+user.podjetje+" "+user.spremembe)
            file.write(user.ime+" "+user.geslo+" "+user.podjetje+" "+user.spremembe+"\n")
        file.close()
        this.readSaveFile()
    def check_password(this,username,password):
        for user in this.users:
            if user.ime==username:
                return user.geslo==password
        return False
    def registriraj(this,ime,geslo,geslo2,podjetje,datum):
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
        this.users.append(uporabnik(ime,geslo,podjetje,"{}"))
        this.writeSaveFile()
        return "Registracija je uspela"
    def getUser(this,ime):
        for user in this.users:
            if user.ime==ime:
                return user
        print("Uporabnika "+ime+" ni mogoče najti")
        return False

