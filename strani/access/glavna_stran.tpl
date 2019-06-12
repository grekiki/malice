% rebase('base.tpl')
%from model import *
%username=user.ime
%podjetje=user.podjetje
<h1>To je spletna stran za naročanje malic.</h1>
<p>Pozdravljeni {{username}} iz {{podjetje}}. Sedaj ste prijavljeni.</p>
<form action="/access/narocila" method="get">
    <input type="submit" value="Spremeni izbiro hrane">
</form>