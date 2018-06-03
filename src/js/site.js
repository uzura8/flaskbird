'use strict';
const util = require('./util.js');

module.exports = {
  configs: require('./config/site.json'),
  uri: function (path) {
    return this.configs.BASE_URL + path.replace(/^\//, '');
  },
  currentUser: function () {
    var elms = document.getElementsByTagName('body');
    var currentUser = elms[0].dataset.currentUser;
    if (util.isEmpty(currentUser)) return {};
    return JSON.parse(currentUser);
  }
}
