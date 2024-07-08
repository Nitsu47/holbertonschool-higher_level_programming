document.addEventListener('DOMContentLoaded', () => {
  const UpdHeader = document.getElementById("update_header");

  UpdHeader.addEventListener('click', () => {
    const header = document.querySelector('header')
    header.textContent = "New Header !!!"
  });
});
