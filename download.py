import os

import urllib3
from dotenv import load_dotenv
load_dotenv()


e = 2023
d = 2

cache_dir = f'cache/{e}'
cache_path = f'{cache_dir}/{d}'
url = f'https://adventofcode.com/{e}/day/{d}/input'
token = os.getenv('token')


def save_new_puzzle_input():
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers={'Cookie':f'session={token}'})
    if r.status != 200:
        raise Exception(f'BAD_REQUEST status_code:{r.status}')
    with open(cache_path, 'w') as f:
        f.write(r.data.decode('utf-8').rstrip('\n'))
        f.close()


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def does_cache_exist(cache_path):
    return os.path.exists(cache_path)


if __name__ == '__main__':
    create_dir(cache_dir)
    if does_cache_exist(cache_path):
        print('puzzle input cached\nExiting...')
    else:
        try:
            save_new_puzzle_input()
            print('saved!')
        except Exception as e:
            print(e)
