import os
import hashlib
from .file import get_file_time
from flask import current_app, g

def url_static(under_static_path):
    env = current_app.config['FLASKBIRD_ENV']
    static_dir_path = current_app.static_url_path
    items = ['app', static_dir_path.strip(os.sep)]
    items.extend(under_static_path.strip(os.sep).split(os.sep))
    path = os.path.join(*items)
    if not os.path.isfile(path):
        return ''

    if env in ['prod', 'stg']:
        if not g.asset_hash:
            g.assset_hash =  hashlib.md5(current_app.config['FLASKBIRD_ENV']).hexdigest()
        asset_hash = g.assset_hash
    else:
        asset_hash = get_file_time(path)
    return '{}/{}?{}'.format(static_dir_path, under_static_path, asset_hash)
