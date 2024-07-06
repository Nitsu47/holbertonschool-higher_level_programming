document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.getElementById('add_item');
  const myList = document.body.querySelector('.my_list');

  addItem.addEventListener('click', () => {
    const li = document.createElement('li');
    li.textContent = 'Item';
    myList.appendChild(li);
  });
});
