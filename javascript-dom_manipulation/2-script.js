document.addEventListener('DOMContentLoaded', function getHeader() {
    const red_header = document.getElementById("red_header");
    const header = document.body.querySelector("header");
    red_header.addEventListener('click', function clickAddClass() {
      header.classList.add('red');
    });
  })
