% rebase('base.tpl')
<%
from model import *
from datetime import *

ctime=datetime.now()
mindate=datum(ctime.day,ctime.month,ctime.year)
if(ctime.hour>=12):
   mindate=datum((ctime+timedelta(days=1)).day,(ctime+timedelta(days=1)).month,(ctime+timedelta(days=1)).year)
end
file=open("datoteke/jedilnik.txt","r")
while True:
    s=file.readline()
    if(len(s)==0):
        break;
    end
    t=s.split(".")
    dan=datum(int(t[0]),int(t[1]),int(t[2]))
    s0="Odjava"
    s1=file.readline()[1:]
    s2=file.readline()[1:]
    s3=file.readline()[1:]
    s4="ocvrti sir s prilogo in solato"
    s5="mesana solata s tuno"
    s6="mesana solata s piscancjimi trakci"
    s7="sadna malica, ki vsebuje 0,70kg sadja in 0,5l navadnega jogurta"
    arr=[s0,s1,s2,s3,s4,s5,s6,s7]
    if(dan==mindate):
        cache=[]
        ans=[0]*8
        for podjetje in model.podjetja:
            ap=[0]*8
            for uporabnik in model.users:
                if(uporabnik.podjetje==podjetje.ime):
                    meni=uporabnik.getMenu(dan)
                    ap[meni]+=1
                    ans[meni]+=1
                end
            end
            cache.append(ap)
        end
%>      
        <h1> Tukaj se belezi statistika malic za {{dan}}</h1>
        <h1>Skupaj</h1><br>
        %for i in range(0,8):
            {{ans[i]}}x {{arr[i]}} <br>
        %end
        <br>
        %for podjetje in model.podjetja:    
            <h1>{{podjetje.ime}}</h1>
            %for i in range(0,8):
                {{ap[i]}}x {{arr[i]}} <br>
            %end
        %end       
%end