import os
from adventofcode import fetch


def read_puzzle_input(cache_path):
    f = open(cache_path, 'r')
    puzzle_input = f.read()
    f.close()
    return puzzle_input


def save_puzzle_input(cache_path, puzzle_input):
    print('Caching puzzle_input...')
    f = open(cache_path, 'w')
    f.write(puzzle_input)
    f.close()
    return puzzle_input


def get_puzzle_input(puzzle_id):
    print('---GET PUZZLE INPUT---')
    cache_path = f'cache/{puzzle_id}'
    if os.path.exists(cache_path):
        print('Cached puzzle_input found...')
        return read_puzzle_input(cache_path)
    else:
        print('No cached puzzle_input found...')
        puzzle_input = fetch()
        return save_puzzle_input(cache_path, puzzle_input)