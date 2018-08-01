import os
import uuid
from flask import current_app
from app import InvalidMediaPathException, NotAcceptableException
from app.common.file import get_ext, write_file
from app.common.image import Image
from app.common.site.util import static_dir_path
from app.media.models import File, FileBin


def media_group_by_mimetype(mimetype):
    media_configs = current_app.config['UPLOAD_ALLOWED_MEDIA']
    for media_group, values in media_configs.items():
        if mimetype in values['types'].values():
            return media_group
    return None


def media_file_name(ext, file_group='', id=0):
    prefix = media_file_prefix(file_group, id)
    randam = uuid.uuid4().hex
    return '{}{}.{}'.format(prefix, randam, ext)


def media_photo_size_infos(size_str):
    accept_sizes = current_app.config['UPLOAD_ALLOWED_MEDIA']['photo']['sizes']
    if size_str not in accept_sizes:
        raise InvalidMediaPathException
    items = size_str.split('x')
    if len(items) < 2:
        raise InvalidMediaPathException
    infos = {'width':int(items[0]), 'height':int(items[1])}
    infos['type'] = 'resize'

    if len(items) == 3:
        if items[2] == 'c':
            infos['type'] = 'crop'

    return infos


def media_file_prefix(file_group='', id=0):
    items = []
    if file_group:
        items.append(file_group)
    if id:
        sprit_count = current_app.config['UPLOAD_SPLIT_DIRS_COUNT']
        split_id = str(id % sprit_count)
        items.append(split_id)
    return '_'.join(items)


def media_dir_path(group='', file_name='', size='', os_path=False):
    items = []
    # ex:  /media
    items.append(current_app.config['MEDIA_DIR_NAME'])
    if not group:
        # ex: /static/media
        return static_dir_path(items, os_path)
    # ex: /media/photo
    items.append(group)

    if not size:
        # ex: /static/media/photo
        return static_dir_path(items, os_path)
    # ex: /media/photo/120x120
    items.append(size)

    if not file_name:
        # ex: /static/media/photo/120x120
        return static_dir_path(items, os_path)
    file_name_parts = file_name.split('_')
    # ex: /media/photo/120x120/m/1/******.jpg
    items.extend(file_name_parts)

    return static_dir_path(items, os_path)


def media_infos_by_req(request_path):
    # ex: /media/photo/120x120/m/1/******.jpg
    media_root_dir = media_dir_path()
    if not request_path.startswith(media_root_dir):
        return

    items = request_path.replace(media_root_dir, '', 1).strip('/').split('/')
    # ex: ['photo' ,'120x120' ,'m' ,'1' ,'******.jpg']
    if not items or len(items) < 4:
        raise InvalidMediaPathException

    group = items.pop(0)
    infos = {'group':group}
    # ex: {'group':'photo'}
    if infos['group'] == 'photo':
        if not len(items) < 5:
            raise InvalidMediaPathException
        size = items.pop(0)
        infos['size'] = size
        # ex: {'group':'photo', 'size':'120x120'}

    infos['name'] = '_'.join(items)
    # ex: {'group':'photo', 'size':'120x120', 'name':'m_1_******.jpg'}

    return infos


def make_media_file(group, name, size='raw'):
    ext = get_ext(name)
    mimetype = current_app.config['UPLOAD_ALLOWED_MEDIA'][group]['types'][ext]
    raw_path = media_dir_path(group, name, 'raw', True)
    if not os.path.exists(raw_path):
        file = File.query.get(name)
        if not file or file.check_deleted():
            raise InvalidMediaPathException
        file_bin = FileBin.query.get(name)
        if not file_bin:
            raise InvalidMediaPathException
        raw_bin = file_bin.get_bin()
        mimetype = file.type
        write_file(raw_path, raw_bin, 'wb')

    if group == 'photo' and size != 'raw':
        path = media_dir_path(group, name, size, True)
        image = Image(raw_path, path)
        size_infos = media_photo_size_infos(size)
        image.resize(**size_infos)
        with open(path, 'rb') as image:
            bin = image.read()
    else:
        path = raw_path
        bin = raw_bin

    return path, name, mimetype, bin


def upload_image(file_strage, media_group, file_group, id):
    accepted_types = current_app.config['UPLOAD_ALLOWED_MEDIA'][media_group]['types']
    mimetype = file_strage.mimetype
    if mimetype not in accepted_types.values():
        raise NotAcceptableException

    ext = get_ext(file_strage.filename)
    if ext not in accepted_types.keys():
        raise NotAcceptableException

    filename = media_file_name(ext, file_group, id)
    size = 'raw' if media_group == 'photo' else None
    path = media_dir_path(media_group, filename, size, True)
    save_path = os.path.dirname(path)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_strage.save(path)
    return [path, filename]


def delete_media_file_caches(group, name, size=None):
    delete_count = 0
    if group != 'photo':
        path = media_dir_path(group, name, None, True)
        if os.path.exists(path):
            os.remove(path)
            delete_count += 1
        return delete_count

    sizes = current_app.config['UPLOAD_ALLOWED_MEDIA']['photo']['sizes']
    for size in sizes:
        path = media_dir_path(group, name, size, True)
        if not os.path.exists(path):
            continue
        os.remove(path)
        delete_count += 1
    return delete_count

