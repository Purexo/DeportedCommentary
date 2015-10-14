/*
var link = document.createElement('link');
link.setAttribute('rel', 'stylesheet');
link.setAttribute('href', '{{host}}/static/awesome-font/css/font-awesome.min.css');

var head = document.getElementsByTagName('head')[0];
head.appendChild(link);
*/
DPCommentary = document.getElementById('DPCommentary');
var xhr = new XMLHttpRequest();
xhr.open('GET', '{{host}}/list', true);
xhr.addEventListener('readystatechange', function() {
	if (xhr.readyState === xhr.DONE && xhr.status === 200)
		DPCommentary.innerHTML = xhr.responseText;
	else 
		DPCommentary.innerHTML = 'La requête n\'a pas aboutie';
}, false);
xhr.send();