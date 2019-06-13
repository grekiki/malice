% rebase('base.tpl')
%from model import *
%username=user.ime
%podjetje=user.podjetje
<h1>To je spletna stran za naročanje malic.</h1>
<p>Pozdravljeni {{username}}. Sedaj ste prijavljeni. Za spremembo jedilnika pritisnite Spremeni izbiro hrane. 
Izbire lahko za jutri spreminjate le do danes do 12. ure. Za poznejše spremembe kontaktirajte osebo odgovorno
za prehrano v podjetju. Če ste sedaj prijavljeni prvič je verjetno smiselno, da spremenite uporabniško ime in geslo.</p>
<form action="/access/narocila" method="get">
    <input type="submit" value="Spremeni izbiro hrane">
</form>
<form action="/access/spremeni_ime" method="get">
    <input type="submit" value="Spremeni ime">
</form>
<form action="/access/spremeni_geslo" method="get">
    <input type="submit" value="Spremeni geslo">
</form>
%if company:
    <form action="/company/manage_users" method="get">
        <input type="submit" value="Nazaj">
    </form>
%else:
    <form action="/access/odjava" method="get">
        <input type="submit" value="Odjava">
    </form>
%end