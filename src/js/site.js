'use strict';
const util = require('./util.js');
const configs =  require('./config/site.json');

module.exports = {
  uri: function (path) {
    return configs.BASE_URL + path.replace(/^\//, '');
  },
  getCurrentUser: function () {
    var elms = document.getElementsByTagName('body');
    var currentUser = elms[0].dataset.currentUser;
    if (util.isEmpty(currentUser)) return {};
    return JSON.parse(currentUser);
  },
  mediaUri: function (file_name, size, type) {
    if (!file_name) return;
    size = String(size || 'raw');
    type = String(type || 'photo');
    var mediaPath = configs.MEDIA_DIR_PATH;
    var items = [mediaPath, type, size].concat(file_name.split('_'));
    return items.join('/');
  }
}
