% rebase('base.tpl')
%username=user.ime
<form action="/change_menu/{{day}}.{{month}}.{{year}}.0", method="get">
    <input type="submit" value="Odjava od malice">
</form>
<form action="/change_menu/{{day}}.{{month}}.{{year}}.1", method="get">
    <input type="submit" value="Prvi meni">
</form>
<form action="/change_menu/{{day}}.{{month}}.{{year}}.2", method="get">
    <input type="submit" value="Drugi meni">
</form>
<form action="/change_menu/{{day}}.{{month}}.{{year}}.3", method="get">
    <input type="submit" value="Tretji meni">
</form>