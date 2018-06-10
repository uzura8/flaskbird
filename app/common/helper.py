import os
import hashlib
from flask import current_app, g
from .file import get_file_time
from .site.util import static_dir_path

def url_static(under_static_path):
    uri_path = static_dir_path(under_static_path)
    env = current_app.config['FLASKBIRD_ENV']
    if env in ['prod', 'stg']:
        if not g.asset_hash:
            app_ver = current_app.config['FLASKBIRD_VERSION']
            g.assset_hash =  hashlib.md5(app_ver).hexdigest()
        asset_hash = g.assset_hash
    else:
        os_path = os.path.join('app', uri_path.lstrip('/'))
        asset_hash = get_file_time(os_path)
    return '{}?{}'.format(uri_path, asset_hash)

def url_media(file_name, size_type='raw', type='photo'):
    media_name = current_app.config['MEDIA_DIR_NAME']
    return static_dir_path('{}/{}/{}/{}'.format(media_name, type,
                                                size_type, file_name))
