'use strict';

var file = document.getElementById('profile_photo');
if (file) {
  file.onchange = function() {
    if (file.files.length > 0) {
      document.getElementById('profile_photo_filename').innerHTML = file.files[0].name;
    }
  };
}
