import os

BASE_DIR = os.path.abspath('.')

def put_to_file(path, data, mode='a'):
    f = open(os.path.join(BASE_DIR, path), mode)
    f.write(data)
    f.close()
