'use strict';

const lib = require('./lib.js');
const axios = lib.axios;
const Vue = lib.Vue;
const i18n = lib.i18n;
const site = lib.site;
const common = require('./common.js');

var app = new Vue({
  i18n: i18n
}).$mount('#container')

