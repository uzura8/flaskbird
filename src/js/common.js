document.addEventListener('DOMContentLoaded', function () {
  // Get all "navbar-burger" elements
  var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {
    // Add a click event on each of them
    $navbarBurgers.forEach(function ($el) {
      $el.addEventListener('click', function () {
        // Get the target from the "data-target" attribute
        var target = $el.dataset.target;
        var $target = document.getElementById(target);
        // Toggle the class on both the "navbar-burger" and the "navbar-menu"
        $el.classList.toggle('is-active');
        if ($target !== null) $target.classList.toggle('is-active');
      });
    });
  }
});

var locale = document.getElementsByTagName('html')[0].getAttribute('lang');

var translations = {
  en: require('./translations/en-message.json'),
  ja: require('./translations/ja-message.json'),
};

var moment = require('moment');
if (locale !== 'en') {
  require('moment/locale/' + locale);
  moment.locale(locale);
}

// axios を require してインスタンスを生成する
const axiosBase = require('axios');
const axios = axiosBase.create({
  baseURL: '/',
  headers: {
    'ContentType': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': locale
  },
  responseType: 'json'
});

exports.locale = locale;
exports.translations = translations;
exports.moment = moment;
exports.axios = axios;

