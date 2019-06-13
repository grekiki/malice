% rebase('base.tpl')
<h1>Spletna stran za naročanje malic</h1>
<p>Če se želite prijaviti ali odjaviti od malice, pritisnite tipko prijava ter vnesite
vaše ime in geslo. Če nadzorujete podjetje potem se prijavite preko tipke Nadzor podjetja. </p>
<form action="/login" method="get">
    <input type="submit" value="Prijava">
</form>
<form action="/company_login" method="get">
    <input type="submit" value="Nadzor podjetja">
</form>
