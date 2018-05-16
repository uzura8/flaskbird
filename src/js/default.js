'use strict';

var common = require('./common.js');
var locale = common.locale;
var translations = common.translations;
var moment = common.moment;
var axios = common.axios;

var Vue = require('vue');

var Buefy = require('buefy');
import 'buefy/lib/buefy.css'
Vue.use(Buefy.default);
//Vue.component(Buefy.default.Loading.name, Buefy.default.Loading);

import VueI18n from 'vue-i18n';
Vue.use(VueI18n);
var i18n = new VueI18n({
  locale: locale,
  fallbackLocale: 'en',
  translations
});

Vue.filter('moment', function (date) {
  return moment(date).format('LLL');
});

//var VueRouter = require('vue-router');
//Vue.use(VueRouter);

var app = new Vue({
  i18n: i18n
}).$mount('#container')

