% rebase('base.tpl')
%from model import *
%from datetime import *
%username=user.ime
%podjetje=user.podjetje
%ctime=datetime.now()
%if(admin):
%   ctime=ctime-timedelta(days=7)
%end
%mindate=datum((ctime+timedelta(days=1)).day,(ctime+timedelta(days=1)).month,(ctime+timedelta(days=1)).year)
%if(ctime.hour>=14):
%   mindate=datum((ctime+timedelta(days=2)).day,(ctime+timedelta(days=2)).month,(ctime+timedelta(days=2)).year)
%end
<h1>Tukaj si izberete menije za vsak dan posebej.</h1>
<form action="/access/main_inside" method="get">
    <input type="submit" value="Nazaj">
</form>
<%
    file=open("datoteke/jedilnik.txt","r")
    while True:
        s=file.readline()
        if(len(s)==0):
            break;
        end
        t=s.split(".")
        dat=datum(int(t[0]),int(t[1]),int(t[2]))
        s0="Odjava"
        s1=file.readline()[1:]
        s2=file.readline()[1:]
        s3=file.readline()[1:]
        s4="ocvrti sir s prilogo in solato"
        s5="mesana solata s tuno"
        s6="mesana solata s piscancjimi trakci"
        s7="sadna malica, ki vsebuje 0,70kg sadja in 0,5l navadnega jogurta"
        arr=[s0,s1,s2,s3,s4,s5,s6,s7]
        if(dat<mindate):
            continue
        end
%>
    <p>
        {{dat.dan_v_tednu_string()}} {{s}}<br>
        %for i in range(0,len(arr)):
        <form action="/access/narocilo/{{str(dat)+"."+str(i)}}" method="post">
             %if user.getMenu(dat)==i:
                <input type="image" src="/img/potrdi.png" border="0" alt="Manjka slika" style="width: 20px;"><b>
            %else:
                <input type="image" src="/img/zavrni.png" border="0" alt="Manjka slika" style="width: 20px;">
            %end
            {{arr[i]}}<br>
            %if user.getMenu(dat)==i:
                </b>
            %end
        </form>
        %end
        <br>
    </p>
%end
%file.close()
