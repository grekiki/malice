import datetime
import json
class uporabnik:
    def __init__(this,ime,geslo,podjetje,spremembe):
        this.ime=ime
        this.geslo=geslo
        this.podjetje=podjetje
        this.spremembe=spremembe
        this.delta=this.parse(spremembe)
        print(this.ime+" "+str(this.delta))
    def parse(this,spremembe):
        seznam=[]
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
                seznam.append(((int(ls[0]),int(ls[1]),int(ls[2])),int(spremembe[1+vejica:zaklepaj])))
        return seznam
    def sprememba(this,datum,stevilo):
        for i in range(0,len(delta)):
            t=this.delta[i]
            if(t[0]==datum):
                this.delta[i]=(datum,stevilo)
                updateStr()
                return
        this.delta.append((datum,stevilo))
        this.updateStr()
    def updateStr(this):
        ans="{"
        for t in this.delta:
            ans+="("+t[0][0]+"."+t[0][1]+"."+t[0][2]+","+t[1]+"),"
        ans+="}"
        this.spremembe=ans
    def getMenu(this,datum):
        for combo in this.delta:
            if(combo[0]==datum):
                return combo[1]
        return 1

class Model:
    def __init__(this):
        this.readSaveFile()
    def readSaveFile(this):
        #print("read")
        file=open("podatki.txt","r")
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
        file=open("podatki.txt","w")
        for user in this.users:
            print(user.ime+" "+user.geslo+" "+user.podjetje+" "+user.spremembe)
            file.write(user.ime+" "+user.geslo+" "+user.podjetje+" "+user.spremembe+"\n")
        file.close()
    def check_password(this,username,password):
        for user in this.users:
            if user.ime==username:
                return user.geslo==password
        return False
    def registriraj(this,ime,geslo,geslo2,podjetje):
        if " " in ime or " " in geslo or len(ime)==0 or len(geslo)==0:
            return False
        for user in this.users:
            if user.ime==ime:
                return False
        if(geslo!=geslo2):
            return False
        this.users.append(uporabnik(ime,geslo,podjetje,"{}"))
        this.writeSaveFile()
        return True
    def dodajSpremembo(this,ime,datum,stevilo):
        for user in this.users:
            if(user.ime==ime):
                user.sprememba(datum,stevilo)
                writeSaveFile()
                return True
        print("Nekaj je narobe v posodobitvah")
        return False
    def getUser(this,ime):
        for user in this.users:
            if user.ime==ime:
                return user
        print("Uporabnika "+ime+" ni mogoče najti")
        return False

