import os
import uuid
from flask import url_for, current_app
from ..util import is_array

def config_js():
    return {
        'BASE_URL': url_for('site.index'),
        'FBD_SITE_NAME': 'FlaskBird',
    }

def media_file_name(group, id, ext):
    prefix = media_file_prefix(group, id)
    randam = uuid.uuid4().hex
    return '{}{}.{}'.format(prefix, randam, ext)

def media_file_prefix(group, id):
    sprit_count = current_app.config['UPLOAD_SPLIT_DIRS_COUNT']
    split_id = id % sprit_count
    return '{}_{}_'.format(group, split_id)

def media_dir_path(media_type, file_name, size=''):
    items = []
    items.append(current_app.config['MEDIA_DIR_NAME'])
    items.append(media_type)
    if size: items.append(size)
    items.append(file_name)
    return static_dir_path(items, True)

def static_dir_path(under_path='', os_path=False):
    static_dir_path = current_app.static_url_path
    if not os_path:
        if is_array(under_path):
            under_path = os.path.join(*under_path)
        return '{}/{}'.format(static_dir_path, under_path)

    items = [static_dir_path.strip(os.sep)]
    items.insert(0, 'app')
    if not is_array(under_path):
        under_path = under_path.strip(os.sep)
    items.extend(under_path)
    return os.path.join(*items)

