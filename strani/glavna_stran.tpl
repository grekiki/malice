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
                    <td bgcolor="FF0000">
                %elif not user.getMenu((ans,month,dateNow.year))==1:
                    <td bgcolor="FFFF00">
                %else:
                    <td>
                %end
                <form action="/date_change", method="get">
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
</body>


<footer>
    Izdelava:Gregor Kikelj
<footer>