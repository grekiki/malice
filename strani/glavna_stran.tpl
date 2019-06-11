% rebase('base.tpl')
%from model import *
%username=user.ime
%podjetje=user.podjetje
<h1>To je spletna stran za naročanje malic.</h1>
<p>Pozdravljeni {{username}} iz {{podjetje}}. Sedaj ste prijavljeni.</p>
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
        {{dat.dan_v_tednu_string()}} {{s}}<br><br>
        {{s1}}<br>
        {{s2}}<br>
        {{s3}}<br>
        {{s4}}<br><br>
    </p>
%end
