% rebase('base.tpl')
%username=user.ime
%podjetje=user.podjetje
<h1>To je spletna stran za naročanje malic.</h1>
<p>Pozdravljeni {{username}} iz {{podjetje}}. Sedaj ste prijavljeni.</p>
%file=open("jedilnik/prazniki.txt","r")