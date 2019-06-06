<!DOCTYPE html>
<html>
<head>
    <title>Naročila malic</title>
</head>


<body bgcolor="CCDDEE">
    <form action="/register_submit", method="post">
        Uporabniško ime:<br>
        <input type="word" name="user">  <br>
        Geslo:<br>
        <input type="password" name="password"><br>
        Ponovi Geslo:<br>
        <input type="password" name="password2"><br>
        Podjetje:<br>
        <select name="podjetje">
            %file=open("podjetja.txt","r")
            %for line in file:
                <option value={{line}}>{{line}}</option>
            %end
        </select><br>
        <input type="submit" value="Registracija">
    </form>
    <b>{{string}}</b>
</body>


<footer>
    Izdelava:Gregor Kikelj
<footer>