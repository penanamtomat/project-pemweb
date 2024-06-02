document.addEventListener('DOMContentLoaded', function () {
  const popupOverlay = document.getElementById('popupOverlay');
  const agreeCheckbox = document.getElementById('agreeCheckbox');
  const continueToReg = document.getElementById('continueToReg');
  const closePopupBtn = document.getElementById('closePopupBttn');

  // popup langsung muncul ketika page pendaftaran di load
  popupOverlay.style.display = 'flex';

  // ketika klik tombol "batal"
  closePopupBtn.addEventListener('click', function () {
    popupOverlay.style.display = 'none';
    agreeCheckbox.checked = false;
    continueToReg.classList.add('hidden');
  });

  // ketika klik checkbox persetujuan
  agreeCheckbox.addEventListener('change', function () {
    // Toggle untuk checkbox menampilkan button "lanjutkan"
    continueToReg.classList.toggle('hidden', !agreeCheckbox.checked);
  });

  // ketika user setuju dan lanjut ke pendaftaran, menghilangkan checklist di checkbox dan menampilkan page pendaftaran
  continueToReg.addEventListener('click', function () {
    agreeCheckbox.checked = false;
    continueToReg.classList.add('hidden');
    popupOverlay.style.display = 'none';
  });

  //form validation
  const submit = document.getElementById('submit');

  submit.addEventListener('click', function (e) {
    const nama = document.getElementById('nama');
    const ttl = document.getElementById('ttl');
    const dadname = document.getElementById('dadname');
    const dadkerja = document.getElementById('dadkerja');
    const momname = document.getElementById('momname');
    const momkerja = document.getElementById('momwork');
    const jk = document.getElementById('jk');
    const nohp = document.getElementById('nohp');
    const alamat = document.getElementById('alamat');
    const jadwal = document.getElementById('jadwal');
    const tahunan = document.getElementById('tahunan');
    const spp = document.getElementById('spp');
    const kk = document.getElementById('kk');

    const cek = document.getElementById('cek');
    if (nama.value == '') {
      cek.classList.add('err');
      cek.classList.remove('hidden');
    } else {
      cek.classList.remove('err');
      cek.classList.add('hidden');
    }

    const cek1 = document.getElementById('cek1');
    if (ttl.value == '') {
      cek1.classList.add('err');
      cek1.classList.remove('hidden');
    } else {
      cek1.classList.remove('err');
      cek1.classList.add('hidden');
    }

    const cek2 = document.getElementById('cek2');
    if (dadname.value == '') {
      cek2.classList.add('err');
      cek2.classList.remove('hidden');
    } else {
      cek2.classList.remove('err');
      cek2.classList.add('hidden');
    }

    const cek3 = document.getElementById('cek3');
    if (dadkerja.value == '') {
      cek3.classList.add('err');
      cek3.classList.remove('hidden');
    } else {
      cek3.classList.remove('err');
      cek3.classList.add('hidden');
    }

    const cek4 = document.getElementById('cek4');
    if (momname.value == '') {
      cek4.classList.add('err');
      cek4.classList.remove('hidden');
    } else {
      cek4.classList.remove('err');
      cek4.classList.add('hidden');
    }

    const cek5 = document.getElementById('cek5');
    if (momkerja.value == '') {
      cek5.classList.add('err');
      cek5.classList.remove('hidden');
    } else {
      cek5.classList.remove('err');
      cek5.classList.add('hidden');
    }

    const cek6 = document.getElementById('cek6');
    if (jk.value == '') {
      cek6.classList.add('err');
      cek6.classList.remove('hidden');
    } else {
      cek6.classList.remove('err');
      cek6.classList.add('hidden');
    }

    const cek7 = document.getElementById('cek7');
    if (nohp.value == '') {
      cek7.classList.add('err');
      cek7.classList.remove('hidden');
    } else {
      cek7.classList.remove('err');
      cek7.classList.add('hidden');
    }

    const cek8 = document.getElementById('cek8');
    if (alamat.value == '') {
      cek8.classList.add('err');
      cek8.classList.remove('hidden');
    } else {
      cek8.classList.remove('err');
      cek8.classList.add('hidden');
    }

    const cek9 = document.getElementById('cek9');
    if (jadwal.value == '') {
      cek9.classList.add('err');
      cek9.classList.remove('hidden');
    } else {
      cek9.classList.remove('err');
      cek9.classList.add('hidden');
    }

    const cek10 = document.getElementById('cek10');
    if (tahunan.value == '') {
      cek10.classList.add('err');
      cek10.classList.remove('hidden');
    } else {
      cek10.classList.remove('err');
      cek10.classList.add('hidden');
    }

    const cek11 = document.getElementById('cek11');
    if (spp.value == '') {
      cek11.classList.add('err');
      cek11.classList.remove('hidden');
    } else {
      cek11.classList.remove('err');
      cek11.classList.add('hidden');
    }

    const cek12 = document.getElementById('cek12');
    if (kk.value == '') {
      cek12.classList.add('err');
      cek12.classList.remove('hidden');
    } else {
      cek12.classList.remove('err');
      cek12.classList.add('hidden');
    }

    if (
      nama.value != '' ||
      ttl.value != '' ||
      dadname.value != '' ||
      dadkerja.value != '' ||
      momname.value != '' ||
      momkerja.value != '' ||
      jk.value != '' ||
      nohp.value != '' ||
      alamat.value != '' ||
      jadwal.value != '' ||
      tahunan.value != '' ||
      spp.value != '' ||
      kk.value != ''
    ) {
      e.preventDefault();
      const popup = document.getElementById('popup');
      const closePopup = document.getElementById('closePopup');

      // popup langsung muncul ketika page pendaftaran di load
      popup.style.display = 'flex';

      // ketika klik tombol "batal"
      closePopup.addEventListener('click', function () {
        popup.style.display = 'none';
      });
    }
  });
});