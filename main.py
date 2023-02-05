import os
import sys
from puzzle_input_cache import build_puzzle_id, read_puzzle_input, save_puzzle_input
from util import leading_zero

from dotenv import load_dotenv
load_dotenv()


if __name__ == '__main__':
	cmd_args = sys.argv[1:]
    if '--generate' in cmd_args:
        save_puzzle_input()
    elif len(cmd_args) == 0:
        print(f'Solution for {build_puzzle_id()}')
        puzzle_input = read_puzzle_input()
        s_module = importlib.import_module(f'Events.{os.getenv('EVENT')}.day{leading_zero(os.getenv('DAY'))}')
        s = s_module.Solution(puzzle_input)
        s.solve()
    else:
        print('UNKNOWN CMD\nEXITING...')