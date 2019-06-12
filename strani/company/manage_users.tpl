% rebase('base.tpl')
<p1>Tukaj lahko spreminjate podatke posameznih zaposlenih</p1>
<form action="/company/main_inside" method="get">
    <input type="submit" value="Nazaj"}>
</form>
%for user in model.users:
%   if user.podjetje==podjetje:
        <form action="/company/redirect/{{user.ime}}" method="get">
            <input type="submit" value={{user.ime}}>
            Prejsnji mesec je bilo narocenih {{user.count_previous_month()}} obrokov.
        </form>
%   end
%end
