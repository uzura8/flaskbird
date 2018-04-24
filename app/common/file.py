import os

BASE_DIR = os.path.abspath('.')

def put_to_file(path, data, mode='a'):
    f = open(os.path.join(BASE_DIR, path), mode)
    f.write(data)
    f.close()

def get_file_time(path, type='edit'):
    abs_path = os.path.join(BASE_DIR, path)
    if type == 'access':
        return os.path.getatime(abs_path)
    elif type == 'create':
        return os.path.getctime(abs_path)
    return os.path.getmtime(abs_path)
