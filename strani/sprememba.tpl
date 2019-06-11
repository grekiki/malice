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
    <form action="/change_menu/{{day}}.{{month}}.{{year}}.0", method="get">
        <input type="submit" value="Odjava od malice">
    </form>
    <form action="/change_menu/{{day}}.{{month}}.{{year}}.1", method="get">
        <input type="submit" value="Prvi meni">
    </form>
    <form action="/change_menu/{{day}}.{{month}}.{{year}}.2", method="get">
        <input type="submit" value="Drugi meni">
    </form>
    <form action="/change_menu/{{day}}.{{month}}.{{year}}.3", method="get">
        <input type="submit" value="Tretji meni">
    </form>
</body>

<a href="/download/junij2019.pdf" download>Jedilnik za junij 2019</a>
<footer>
    Izdelava:Gregor Kikelj
<footer>