let menu = document.getElementById('menu');
let li = document.createElement('li');
li.textContent = 'the inside text';
menu.replaceChild(li, menu.firstChild);