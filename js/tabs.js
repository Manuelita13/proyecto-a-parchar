const triggerTabList = document.querySelectorAll('#v-pills-tab button');
triggerTabList.forEach(triggerEl => {
  const tabTrigger = new bootstrap.Tab(triggerEl);

  triggerEl.addEventListener('click', event => {
    event.preventDefault();
    tabTrigger.show();
  });
});