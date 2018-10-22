"use strict";

function clearComment() {
    // clear the name and comment
    document.getElementById('namebox').value = 'Name';
    document.getElementById('txtbox').value = '';
}

function addComment() {
    // add a comment then clear the form
    var ctxt = document.getElementById('txtbox').value;
    var cname = document.getElementById('namebox').value;
    if (cname === 'Name'){
        cname = 'Anon';
    }
    var comment = 'Comment: name=' + cname + ', text=' + ctxt;
    // alert(comment);
    saveComment(comment);
    clearComment();
}

function saveComment(comment) {
    // save the comment to the list
    var node = document.createElement('li');
    var textNode = document.createTextNode(comment);
    node.appendChild(textNode);
    document.getElementById('cmtList').appendChild(node);
}
