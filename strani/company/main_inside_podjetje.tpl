% rebase('base.tpl')
<h1>Glavna stran podjetja {{podjetje}}.</h1> 
<p>Tukaj lahko upravljate s podatki vseh zaposlenih v 
vašem podjetju. To naredite z gumbom Upravljanje računov.</p>
<p>Če kateri od zaposlenih pozabi geslo mu ga lahko preko te strani ponastavite. Zaposlenim lahko tudi spremenite uporabniško ime.
Če kdo od zaposlenih zboli ga lahko odjavite od malice. Za spremembo malice za jutri imate čas do danes do 12. ure. Če bi
odjavo radi naredili pozneje, potem pokličite v podjetje."
<form action="/company/manage_users" method="get">
    <input type="submit" value="Upravljanje racunov"}>
</form>
<form action="/company/change_password" method="get">
    <input type="submit" value="Sprememba gesla"}>
</form>
<form action="/company/odjava" method="get">
    <input type="submit" value="Odjava"}>
</form>