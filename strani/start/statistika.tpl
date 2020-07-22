% rebase('base.tpl')
<h1> Tukaj se belezi statistika malic za {{dan}}</h1>
<h1>Skupaj</h1><br>
%for i in range(0,8):
    {{ans[i]}}x {{arr[i]}} <br>
%end
<br>
%for i in range(0,len(model.podjetja)):
    %podjetje=model.podjetja[i]
    <h1>{{podjetje.ime}}</h1>
    %for j in range(0,8):
        {{cache[i][j]}}x {{arr[j]}} <br>
    %end
%end       
