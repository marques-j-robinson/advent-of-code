import os
import importlib
from cache_layer import get_puzzle_input
from util import leading_zero

from dotenv import load_dotenv
load_dotenv()

event = os.getenv('EVENT')
day = leading_zero(os.getenv('DAY'))
puzzle_id = f'{event}_{day}'


def import_solution():
    return importlib.import_module(f'Events.{event}.day{day}')


if __name__ == '__main__':
    print(f'puzzle_id:{puzzle_id}')
    puzzle_input = get_puzzle_input(puzzle_id)
    s = import_solution()
    print(f'---SOLVING---')
    print(f'Part 1: {s.p1(puzzle_input)}')
    print(f'Part 2: {s.p2(puzzle_input)}')
