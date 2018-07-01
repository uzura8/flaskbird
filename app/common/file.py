import os, json

BASE_DIR = os.path.abspath('.')

def put_to_file(path, data, mode='a'):
    f = open(os.path.join(BASE_DIR, path), mode)
    f.write(data)
    f.close()

def put_json_from_dict(path, data_dict, json_format={}, mode='w'):
    if not json_format:
        json_format = {
            'indent': 4,
            'separators':(',', ': ')
        }
    with open(path, mode) as f:
        json.dump(data_dict, f)

def get_file_time(path, type='edit'):
    abs_path = os.path.join(BASE_DIR, path)
    if type == 'access':
        return os.path.getatime(abs_path)
    elif type == 'create':
        return os.path.getctime(abs_path)
    return os.path.getmtime(abs_path)

def get_ext(filename, is_lower=True):
    ext = filename.rsplit('.', 1)[1]
    return ext.lower() if is_lower else ext

def write_file(file_path, data, mode='w'):
    dir_path = os.path.dirname(file_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(file_path, mode) as fp:
        fp.write(data)
