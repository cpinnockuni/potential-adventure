let toggle = document.getElementById('toggle');
let close = document.getElementById('close');
let menu = document.getElementById('menu');

toggle.addEventListener('click', function() {
  menu.classList.remove('hide');
});

close.addEventListener('click', function() {
  menu.classList.add('hide');
});