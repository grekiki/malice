% rebase('base.tpl')
<form action="/company_login", method="post">
    Podjetje:<br>
    <select name="podjetje">
        %file=open("datoteke/podjetja.txt","r")
        %for line in file:
            <option value={{line.split(" ")[0]}}>{{line.split(" ")[0]}}</option>
        %end
    </select><br>
    Geslo:<br>
    <input type="password" name="password"><br>
    <input type="submit" value="Prijava">
</form>
<b>{{string}}</b>