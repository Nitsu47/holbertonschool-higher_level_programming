document.addEventListener('DOMContentLoaded', function getHeader() {
  const toggle_header = document.getElementById("toggle_header");
  const header = document.body.querySelector("header");
  toggle_header.addEventListener('click', function clickToggleClass() {
    header.classList.toggle('red');
    header.classList.toggle('green');
  });
})
