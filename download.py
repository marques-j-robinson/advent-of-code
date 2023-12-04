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


def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


if __name__ == '__main__':
    create_dir(f'cache/{e}')
    print('hi')
