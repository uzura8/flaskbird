'use strict';

const common = require('./common.js');
const locale = common.locale;
const translations = common.translations;
const moment = common.moment;
const axios = common.axios;

var Vue = require('vue');

var Buefy = require('buefy');
Vue.use(Buefy.default);
//import 'buefy/lib/buefy.css'
//Vue.component(Buefy.default.Loading.name, Buefy.default.Loading);

import VueI18n from 'vue-i18n';
Vue.use(VueI18n);
var i18n = new VueI18n({
  locale: locale,
  fallbackLocale: 'en',
  messages: translations
});

Vue.filter('moment', function (date) {
  return moment(date).format('LLL');
});

//var VueRouter = require('vue-router');
//Vue.use(VueRouter);

var app = new Vue({
  i18n: i18n
}).$mount('#container')

