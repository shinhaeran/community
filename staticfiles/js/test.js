function reComment(comment_id, app_name, token) {

    var a = document.createElement("form");
    a.setAttribute('method', "POST");
    a.setAttribute('action', "/"+app_name+"/"+comment_id+"/addReComment");
    a.setAttribute('id', comment_id+'reCoMment')

    var b = document.createElement("input");
    b.type = "text";
    b.name = "text";     //name 에는 모델 내에 있는 field명을 적어줘야한다.

    var c = document.createElement("input");
    c.type = "submit";
    c.value = "작성";

    var d = document.createElement("input");
    d.setAttribute('name', 'csrfmiddlewaretoken');
    d.setAttribute('value', token);
    d.type = "hidden";
    
    a.appendChild(b);
    a.appendChild(c);
    a.appendChild(d);
    
    document.getElementById(comment_id+'form').appendChild(a);
}