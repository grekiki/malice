% rebase('base.tpl')
<form action="/company/change_password" method="post">
    Novo geslo:<br>
    <input type="password" name="geslo1">  <br>
    Potrdi novo geslo:<br>
    <input type="password" name="geslo2">  <br>
    <input type="submit" value="Potrdi spremembo">
</form>
<b>{{string}}</b>