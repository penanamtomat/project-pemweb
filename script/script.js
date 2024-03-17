document.addEventListener('DOMContentLoaded', function() {
    const popupOverlay = document.getElementById('popupOverlay');
    const agreeCheckbox = document.getElementById('agreeCheckbox');
    const popupReg = document.getElementById('popupReg');
    const continueToReg = document.getElementById('continueToReg');
    const closePopupBtn = document.getElementById('closePopupBttn');
    


    // ketika user klik link "Daftar"
    popupReg.addEventListener('click', function(event) {
        // biar ga langsung ke halaman daftar
        event.preventDefault();

        // Membuka pop-up peringatan
        popupOverlay.style.display = 'flex';
    });

    // ketika klik tombol "batal"
    closePopupBtn.addEventListener('click', function() {
        popupOverlay.style.display = 'none';
        agreeCheckbox.checked = false;
        continueToReg.classList.add('hidden');
    });

    // ketika klik checkbox persetujuan
    agreeCheckbox.addEventListener('change', function() {
        // Toggle untuk checkbox menampilkan button "lanjutkan"
        continueToReg.classList.toggle('hidden', !agreeCheckbox.checked);
    });

    // ketika user setuju dan lanjut ke pendaftaran, menghilangkan checklist di checkbox jika user kembali ke landing page
    continueToReg.addEventListener('click', function(){
        agreeCheckbox.checked = false;
        continueToReg.classList.add('hidden');
    });
});
