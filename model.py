class uporabnik:
    def __init__(this,ime,geslo,podjetje,spremembe):
        this.ime=ime
        this.geslo=geslo
        this.podjetje=podjetje
        this.spremembe=spremembe

class Model:
    def __init__(this):
        this.readSaveFile()
    def readSaveFile(this):
        print("read")
        file=open("podatki.txt","r")
        this.users=[]
        for line in file:
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
        for user in this.users:
            if user.ime==ime:
                return False
        if(geslo!=geslo2):
            return False
        this.users.append(uporabnik(ime,geslo,podjetje,"{}"))
        this.writeSaveFile()
        return True
