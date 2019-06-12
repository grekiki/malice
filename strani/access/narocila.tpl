% rebase('base.tpl')
%from model import *
%username=user.ime
%podjetje=user.podjetje
<h1>Tukaj si izberete menije za vsak dan posebej.</h1>
<%
    file=open("datoteke/jedilnik.txt","r")
    while True:
        s=file.readline()
        if(len(s)==0):
            break;
        end
        t=s.split(".")
        dat=datum(int(t[0]),int(t[1]),int(t[2]))
        s1=file.readline()[1:]
        s2=file.readline()[1:]
        s3=file.readline()[1:]
        s4="Odjava"
%>
    <p>
        {{dat.dan_v_tednu_string()}} {{s}}<br>
        <form action="/access/narocilo/{{str(dat)+".1"}}" method="get">
            
            %if user.getMenu(dat)==1:
                <input type="image" src="/img/potrdi.png" border="0" alt="Manjka slika" style="width: 20px;">
            %else:
                <input type="image" src="/img/zavrni.png" border="0" alt="Manjka slika" style="width: 20px;">
            %end
            {{s1}}<br>
        </form>
        <form action="/access/narocilo/{{str(dat)+".2"}}" method="get">
            %if user.getMenu(dat)==2:
                <input type="image" src="/img/potrdi.png" border="0" alt="Manjka slika" style="width: 20px;">
            %else:
                <input type="image" src="/img/zavrni.png" border="0" alt="Manjka slika" style="width: 20px;">
            %end
            {{s2}}<br>
        </form>
        <form action="/access/narocilo/{{str(dat)+".3"}}" method="get">
             %if user.getMenu(dat)==3:
                <input type="image" src="/img/potrdi.png" border="0" alt="Manjka slika" style="width: 20px;">
            %else:
                <input type="image" src="/img/zavrni.png" border="0" alt="Manjka slika" style="width: 20px;">
            %end
            {{s3}}<br>
        </form>
        <form action="/access/narocilo/{{str(dat)+".0"}}" method="get">
             %if user.getMenu(dat)==0:
                <input type="image" src="/img/potrdi.png" border="0" alt="Manjka slika" style="width: 20px;">
            %else:
                <input type="image" src="/img/zavrni.png" border="0" alt="Manjka slika" style="width: 20px;">
            %end
            {{s4}}<br><br>
        </form>
    </p>
%end
%file.close()
