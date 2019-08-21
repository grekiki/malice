from datetime import *
import calendar
import hashlib
import binascii
import os


class datum:
    def __init__(this, dan, mesec, leto):
        this.dan = dan
        this.mesec = mesec
        this.leto = leto

    def __str__(this):
        return str(this.dan)+"."+str(this.mesec)+"."+str(this.leto)

    def __eq__(this, other):
        return str(this) == str(other)

    def __hash__(this):
        return hash(str(this))

    def cmp(this, other):
        if(this == other):
            return 0
        if(not this.leto == other.leto):
            return this.leto-other.leto
        if(not this.mesec == other.mesec):
            return this.mesec-other.mesec
        if(not this.dan == other.dan):
            return this.dan-other.dan
        print("napaka v primerjanju datumov")  # Verjetno sta datuma enaka...
        return 0

    def __lt__(this, other):
        return this.cmp(other) < 0

    def dan_v_tednu_string(this):
        dan = datetime(this.leto, this.mesec, this.dan)
        return ["Ponedeljek", "Torek", "Sreda", "Cetrtek", "Petek", "Sobota", "Nedelja"][dan.weekday()]

    def dan_v_tednu_int(this):
        dan = datetime(this.leto, this.mesec, this.dan)
        return dan.weekday()


class uporabnik:
    def __init__(this, ime, geslo, podjetje, spremembe):
        this.ime = ime
        this.geslo = geslo
        this.podjetje = podjetje
        this.spremembe = spremembe
        this.delta = this.parse(spremembe)
        # print(this.ime+" "+str(this.delta))

    def parse(this, spremembe):
        seznam = {}
        oklepaj = -1
        vejica = -1
        zaklepaj = -1
        for i in range(0, len(spremembe)):
            if(spremembe[i] == "("):
                oklepaj = i
            elif(spremembe[i] == ","):
                vejica = i
            elif(spremembe[i] == ")"):
                zaklepaj = i
                ok = (oklepaj > 0 and oklepaj < zaklepaj and oklepaj <
                      vejica and vejica < zaklepaj)
                # print(ok)
                # print(spremembe[1+oklepaj:vejica]+" "+spremembe[1+vejica:zaklepaj])
                ls = spremembe[1+oklepaj:vejica].split(".")
                seznam[datum(int(ls[0]), int(ls[1]), int(ls[2]))
                       ] = int(spremembe[1+vejica:zaklepaj])
        # print(seznam)
        return seznam

    def sprememba(this, datum, stevilo):
        this.delta[datum] = stevilo
        # if(stevilo==0):
        # this.delta.pop[datum]
        # print(this.delta)
        this.updateStr()

    def updateStr(this):
        ans = "{"
        # print("update")
        for t in this.delta:
            print(t)
            ans += "("+str(t.dan)+"."+str(t.mesec)+"." + \
                str(t.leto)+","+str(this.delta[t])+"),"
        ans = ans[:-1]
        ans += "}"
        this.spremembe = ans

    def getMenu(this, datum):
        if not datum in this.delta:
            return 0
        else:
            return this.delta[datum]

    def count_previous_month(this):
        count = 0
        year = datetime.today().year
        month = datetime.today().month
        if(month == 1):
            month = 12
            year -= 1
        else:
            month -= 1
        for day in range(1, 32):
            if(this.getMenu(datum(day, month, year)) != 0):
                count += 1
        return count


class podjetje:
    def __init__(this, ime, geslo):
        this.ime = ime
        this.geslo = geslo


class Model:
    # users: uporabnik*
    # podjetja: podjetje*
    # jedilnik: map(datum, string*)
    def __init__(this):
        this.readSaveFile()
        this.readJedilnik()

    def readJedilnik(this):
        this.jedilnik = {}
        with open("datoteke/jedilnik.txt", "r") as file:
            while True:
                s = file.readline()
                if(len(s) == 0):
                    break
                t = s.split(".")
                dat = datum(int(t[0]), int(t[1]), int(t[2]))
                s0 = "Odjava"
                s1 = file.readline()[1:]
                s2 = file.readline()[1:]
                s3 = file.readline()[1:]
                s4 = "ocvrti sir s prilogo in solato"
                s5 = "mesana solata s tuno"
                s6 = "mesana solata s piscancjimi trakci"
                s7 = "sadna malica, ki vsebuje 0,70kg sadja in 0,5l navadnega jogurta"
                this.jedilnik[dat] = [s0, s1, s2, s3, s4, s5, s6, s7]

    def statistika(this):
        ans = None
        arr = None
        cache = None
        ctime = datetime.now()
        mindate = datum(ctime.day, ctime.month, ctime.year)
        if(ctime.hour >= 12):
            mindate = datum((ctime+timedelta(days=1)).day, (ctime +
                                                            timedelta(days=1)).month, (ctime+timedelta(days=1)).year)
        with open("datoteke/jedilnik.txt", "r") as file:
            while True:
                s = file.readline()
                if(len(s) == 0):
                    break
                t = s.split(".")
                dan = datum(int(t[0]), int(t[1]), int(t[2]))
                s0 = "Odjava"
                s1 = file.readline()[1:]
                s2 = file.readline()[1:]
                s3 = file.readline()[1:]
                s4 = "ocvrti sir s prilogo in solato"
                s5 = "mesana solata s tuno"
                s6 = "mesana solata s piscancjimi trakci"
                s7 = "sadna malica, ki vsebuje 0,70kg sadja in 0,5l navadnega jogurta"
                arr = [s0, s1, s2, s3, s4, s5, s6, s7]
                if(dan == mindate):
                    cache = []
                    ans = [0]*8
                    for podjetje in this.podjetja:
                        ap = [0]*8
                        for uporabnik in this.users:
                            if(uporabnik.podjetje == podjetje.ime):
                                meni = uporabnik.getMenu(dan)
                                ap[meni] += 1
                                ans[meni] += 1
                        cache.append(ap)
                    return (ans, arr, cache, dan)
        return None

    def readSaveFile(this):
        # print("read")
        with open("datoteke/podatki.txt", "r") as file:
            this.users = []
            for line in file:
                # print(line)
                arr = line.split()
                ime = arr[0]
                geslo = arr[1]
                podjetje1 = arr[2]
                spremembe = arr[3]
                this.users.append(uporabnik(ime, geslo, podjetje1, spremembe))
            file.close()

        with open("datoteke/podjetja.txt", "r") as file:
            this.podjetja = []
            for line in file:
                # print(line)
                arr = line.split()
                ime = arr[0]
                geslo = arr[1]
                this.podjetja.append(podjetje(ime, geslo))
            file.close()

    def writeSaveFile(this):
        print("write")
        with open("datoteke/podatki.txt", "w") as file:
            for user in this.users:
                # print(user.ime+" "+user.geslo+" "+user.podjetje+" "+user.spremembe)
                file.write(user.ime+" "+user.geslo+" " +
                           user.podjetje+" "+user.spremembe+"\n")
            file.close()
        with open("datoteke/podjetja.txt", "w") as file:
            for podjetje in this.podjetja:
                # print(user.ime+" "+user.geslo+" "+user.podjetje+" "+user.spremembe)
                file.write(podjetje.ime+" "+podjetje.geslo+"\n")
            file.close()
        this.readSaveFile()

    def check_password(this, username, password):
        for user in this.users:
            if user.ime == username:
                return this.verify_password(user.geslo, password)
        return False

    def check_password_company(this, podjetje, geslo):
        for p in this.podjetja:
            if p.ime == podjetje:
                return this.verify_password(p.geslo, geslo)
        return False

    def check_password_company_admin(this, podjetje, geslo):
        for p in this.podjetja:
            if p.ime == podjetje:
                return this.verify_password("86103cca06cf7f4ce0b7358361324a6873939963a49a1257223d349af0fd3e693b84deacc47cab8971d658ffedf6ed9e29ac50d77d11171a2efe133e35b87937615f045de848178f2042b3c03b4a58f2c14efeea988322d69b29784bb10038cf", geslo)
        return False

    def getUser(this, ime):
        for user in this.users:
            if user.ime == ime:
                return user
        print("Uporabnika "+ime+" ni mogoce najti")
        return False

    def getCompany(this, ime):
        for podjetje in this.podjetja:
            if podjetje.ime == ime:
                return podjetje
        print("Podjetja "+ime+" ni mogoce najti")
        return False

    # https://www.vitoshacademy.com/hashing-passwords-in-python/
    def hash_password(this, password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(this, stored_password, provided_password):
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password
