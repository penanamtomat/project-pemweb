const hamBurger = document.querySelector('#toggle-btn');

hamBurger.addEventListener('click', function () {
  document.querySelector('#sidebar').classList.toggle('expand');
});

// js logout

const logout = document.getElementById('logout');
logout.addEventListener('click', function (event) {
  const popupOverlay = document.getElementById('popupOverlay');
  const closePopupBtn = document.getElementById('closePopupBttn');

  event.preventDefault();

  // popup langsung muncul ketika page pendaftaran di load
  popupOverlay.style.display = 'flex';

  // ketika klik tombol "batal"
  closePopupBtn.addEventListener('click', function () {
    popupOverlay.style.display = 'none';
  });
});

const log = document.getElementById('log');
log.addEventListener('click', function (event) {
  const popupOverlay = document.getElementById('popupOverlay');
  const closePopupBtn = document.getElementById('closePopupBttn');

  event.preventDefault();

  // popup langsung muncul ketika page pendaftaran di load
  popupOverlay.style.display = 'flex';

  // ketika klik tombol "batal"
  closePopupBtn.addEventListener('click', function () {
    popupOverlay.style.display = 'none';
  });
});
