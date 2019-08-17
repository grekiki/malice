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
%for key,value in model.jedilnik.items():
    %if(key<mindate):
        %continue;
    %end
    <p>
    {{key.dan_v_tednu_string()}} {{key}}<br>
    %for i in range(0,len(value)):
        <form action="/access/narocilo/{{str(key)+"."+str(i)}}" method="post">
            %if user.getMenu(key)==i:
                <input type="image" src="/img/potrdi.png" border="0" alt="Manjka slika" style="width: 20px;"><b>
            %else:
                <input type="image" src="/img/zavrni.png" border="0" alt="Manjka slika" style="width: 20px;">
            %end
            {{value[i]}}<br>
            %if user.getMenu(key)==i:
                </b>
            %end
        </form>
    %end
    <br>
    </p>     
%end
