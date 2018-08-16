'use strict';

// axios を require してインスタンスを生成する
import axiosBase from 'axios';
const axios = axiosBase.create({
  baseURL: '/',
  headers: {
    'ContentType': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': locale
  },
  responseType: 'json'
});


var Vue = require('vue');

var Buefy = require('buefy');
Vue.use(Buefy.default);

import VueI18n from 'vue-i18n';
Vue.use(VueI18n);
var locale = document.getElementsByTagName('html')[0].getAttribute('lang');
var translations = {
  en: require('./translations/en-message.json'),
  ja: require('./translations/ja-message.json'),
};
var i18n = new VueI18n({
  locale: locale,
  fallbackLocale: 'en',
  messages: translations
});

import moment from 'moment';
if (locale !== 'en') {
  require('moment/locale/' + locale);
  moment.locale(locale);
}
Vue.filter('moment', function (date) {
  return moment(date).format('LLL');
});

const site = require('./site.js');
Vue.mixin({
  methods: {
    siteUri: site.uri,
    mediaUri: site.mediaUri,
    getCurrentUser: site.getCurrentUser
  }
});

export {axios, Vue, i18n, site};
