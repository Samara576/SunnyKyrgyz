// Объект с переводами
const translations = {
  ru: {
    headline_start: "Там, где горы касаются неба – начни своё",
    headline_end: "путешествие с",
    about: "О нас",
    contact: "Контакты",
    login: "Войти",
    register: "Зарегистрироваться",
    tours: "Тур и маршруты",
    housing: "Жильё",
    agromarket: "AgroMarket",
    company: "SunnyKyrgyzstan"
  },
  kg: {
    headline_start: "Тоонун чокусу асманга тийген жерде –",
    headline_end: "саякатыңды SunnyKyrgyzstan менен башта", // тут уже включено имя
    about: "Биз жөнүндө",
    contact: "Байланыш",
    login: "Кирүү",
    register: "Катталуу",
    tours: "Тур жана багыттар",
    housing: "Турак жай",
    agromarket: "AgroMarket",
    company: "" // чтобы в HTML не вставлялось лишнее
  },
  en: {
    headline_start: "In the land where the sky touches the peaks – discover your",
    headline_end: "adventure with",
    about: "About us",
    contact: "Contact",
    login: "Login",
    register: "Register",
    tours: "Tours & Routes",
    housing: "Hotels",
    agromarket: "AgroMarket",
    company: "SunnyKyrgyzstan"
  }
};

// Кнопки для смены языка
const langButtons = document.querySelectorAll(".lang-btn");
// Элементы с data-i18n
const elements = document.querySelectorAll("[data-i18n]");

// Функция смены языка
function setLanguage(lang) {
  localStorage.setItem("lang", lang);

  elements.forEach(el => {
    const key = el.getAttribute("data-i18n");
    const translation = translations[lang][key];
    if (translation !== undefined) {
      el.innerText = translation;
    }
  });

  // Управляем отображением "SunnyKyrgyzstan" отдельно
  const brand = document.getElementById("brand-name");
  if (brand) {
    brand.style.display = (lang === "kg") ? "none" : "inline";
  }
}

// Установка языка при загрузке
const savedLang = localStorage.getItem("lang") || "ru";
setLanguage(savedLang);

// Обработчики на кнопки
langButtons.forEach(btn => {
  btn.addEventListener("click", () => {
    const lang = btn.getAttribute("data-lang");
    setLanguage(lang);
  });
});
