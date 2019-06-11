<!DOCTYPE html>
<html>
<head>
    <title>Naročila malic</title>
    <style>
    table { 
        table-layout:fixed; width:700px;
    }
    table tr {
        height: 80px;
    }
</style>
</head>


<body bgcolor="CCDDEE">
    %username=user.ime
    %podjetje=user.podjetje
    <h1>To je spletna stran za naročanje malic.</h1>
    <p>Pozdravljeni {{username}} iz {{podjetje}}. Sedaj ste prijavljeni.</p>
    %from datetime import *
    %from calendar import monthrange
    %dateNow=datetime.today()
    %dateInit=date(dateNow.year,dateNow.month,1)
    %ln=monthrange(dateNow.year,dateNow.month)[1]
    %displacement=dateInit.weekday()
    %month=dateNow.month
    %color=["FF0000","00FF00","FF00FF","0000FF"]
    %year=dateNow.year
    <table border="1">
    %p=0
    %for row in range(0,6):
        <tr>
        %for col in range(0,7):
            %if p<displacement:
                <td></td>
            %elif p<displacement+ln:
                %ans=p-displacement+1
                %if ans==dateNow.day:
                    <td bgcolor="000000">
                %elif True:
                    %ans2=color[user.getMenu((ans,month,dateNow.year))]
                    <td bgcolor={{ans2}}>
                %else:
                    <td>
                %end
                <form action="/date_change/{{ans}}.{{month}}.{{year}}", method="get">
                    <input type="submit" value={{ans}}.{{month}} name={{ans}}>
                </form>
                </td>
            %else:
                <td></td>
            %end
            %p+=1
        %end
        </tr>
    %end
    </table>
</body>

<a href="/download/junij2019.pdf" download>Jedilnik za junij 2019</a>
<footer>
    Izdelava:Gregor Kikelj
<footer>