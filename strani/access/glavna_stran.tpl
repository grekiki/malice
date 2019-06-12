% rebase('base.tpl')
%from model import *
%username=user.ime
%podjetje=user.podjetje
<h1>To je spletna stran za naročanje malic.</h1>
<p>Pozdravljeni {{username}}. Sedaj ste prijavljeni.</p>
<form action="/access/narocila" method="get">
    <input type="submit" value="Spremeni izbiro hrane">
</form>
<form action="/access/spremeni_ime" method="get">
    <input type="submit" value="Spremeni ime">
</form>
<form action="/access/spremeni_geslo" method="get">
    <input type="submit" value="Spremeni geslo">
</form>
<form action="/access/odjava" method="get">
    <input type="submit" value="Odjava">
</form>