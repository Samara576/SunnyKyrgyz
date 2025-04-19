document.addEventListener("DOMContentLoaded", () => {
    const nav = document.querySelector(".nav-links");
  
    // проверим, вошёл ли пользователь
    const isLoggedIn = localStorage.getItem("loggedIn");
  
    if (isLoggedIn === "true") {
      nav.innerHTML = `
        <a href="about.html" data-i18n="about">О нас</a>
        <a href="contact.html" data-i18n="contact">Контакты</a>
        <a href="profile.html" data-i18n="profile">Личный профиль</a>
      `;
    }
  });
  