import os

import urllib3
from dotenv import load_dotenv
load_dotenv()


e = 2015
d = 1

url = f'https://adventofcode.com/{e}/day/{d}/input'
token = os.getenv('TOKEN')
headers = {'Cookie':f'session={token}'}


def save_new_puzzle_input():
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers=headers)
    return r.data.decode('utf-8').rstrip('\n')


def check_cache_dir():
    if not os.path.exists('cache'):
        os.makedirs('cache')


if __name__ == '__main__':
    check_cache_dir()
    print('hi')
