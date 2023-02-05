import os
from get_puzzle_input import get_puzzle_input
from util import leading_zero


def build_puzzle_id():
    event = os.getenv('EVENT')
    day = os.getenv('DAY')
    return f'{event}_{leading_zero(day)}'


def build_cache_path():
    return f'cache/{build_puzzle_id(event, day)}'


def read_puzzle_input():
    f = open(build_cache_path(event, day), 'r')
    puzzle_input = f.read()
    f.close()
    return puzzle_input


def save_puzzle_input():
    cache_path = build_cache_path(event, day)
    if os.path.exists(cache_path):
        print(f'{build_puzzle_id()} PUZZLE INPUT ALREADY STORED IN CACHE!')
    else:
        puzzle_input = get_puzzle_input()
        f = open(cache_path, 'w')
        f.write(puzzle_input)
        f.close()
        print(f'Stored puzzle_input in cache at {cache_path}')