const submit = document.getElementById("submit");
const username = document.getElementById("username");
const password = document.getElementById("password");

submit.addEventListener("click", function (e) {
  e.preventDefault();

if (username.value == "" || password.value == "") {
    alert("Please fill out all fields");
} else if (username.value == "admin" && password.value == "1234") {
    window.location.replace("dashboard.html");
} else if (username.value == "guru" && password.value == "124") {
    window.location.href = "absenGuru.html";
} else if (username.value == "santri" && password.value == "123") {
    window.location.href = "dashboardSantri.html";
}  else if (username.value == "admin" && password.value != "1234" ) {
    alert("password salah");
} else if (username.value == "guru" && password.value != "124") {
    alert("password salah");
}  else if (username.value == "santri" && password.value != "123") {
    alert("password salah");
} else {
    const popupOverlay = document.getElementById("popupOverlay");
    const closePopupBtn = document.getElementById("closePopupBttn");

    // popup langsung muncul ketika page pendaftaran di load
    popupOverlay.style.display = "flex";

    // ketika klik tombol "batal"
    closePopupBtn.addEventListener("click", function () {
      popupOverlay.style.display = "none";
    });
}
});