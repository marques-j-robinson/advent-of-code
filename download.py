import os

import urllib3
from dotenv import load_dotenv
load_dotenv()


e = 2015
d = 1

cache_dir = f'cache/{e}'
url = f'https://adventofcode.com/{e}/day/{d}/input'
token = os.getenv('TOKEN')
headers = {'Cookie':f'session={token}'}


def save_new_puzzle_input():
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers=headers)
    return r.data.decode('utf-8').rstrip('\n')


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def does_cache_exist(cache_path):
    return os.path.exists(cache_path)


if __name__ == '__main__':
    create_dir(cache_dir)
    if does_cache_exist(f'{cache_dir}/{d}'):
        print(f'puzzle input cached\nExiting...')
