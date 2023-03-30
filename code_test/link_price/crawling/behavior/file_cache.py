import os
import pickle

cache_dir = os.path.join(os.getcwd(), './cache')
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

def get_cache_filename(key):
    return os.path.join(cache_dir, '{}.pickle'.format(key))

def load_cache(key):
    cache_filename = get_cache_filename(key)
    if os.path.exists(cache_filename):
        with open(cache_filename, 'rb') as f:
            return pickle.load(f)
    else:
        return None

def save_cache(key, data):
    cache_filename = get_cache_filename(key)
    with open(cache_filename, 'wb') as f:
        pickle.dump(data, f)