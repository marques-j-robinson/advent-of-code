import os
import sys
from puzzle_input_cache import build_puzzle_id, read_puzzle_input, save_puzzle_input
from util import leading_zero

from dotenv import load_dotenv
load_dotenv()


def cmd_args():
    return sys.argv[1:]


def generate():
    if '--generate' in cmd_args():
        save_puzzle_input()


def build_module_filename():
    event = os.getenv('EVENT')
    day = leading_zero(os.getenv('DAY'))
    return importlib.import_module(f'Events.{event}.day{day}')


def solve():
    if len(cmd_args()) == 0:
        print(f'Solution for {build_puzzle_id()}')
        puzzle_input = read_puzzle_input()
        s_module = build_module_filename()
        s = s_module.Solution(puzzle_input)
        s.solve()


if __name__ == '__main__':
    generate()
    solve()