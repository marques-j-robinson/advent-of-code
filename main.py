import os
import importlib

from dotenv import load_dotenv
load_dotenv()

from format_string import leading_zero


event = os.getenv('EVENT')
day = leading_zero(os.getenv('DAY'))


def import_solution_module():
    return importlib.import_module(f'Events.{event}.day{day}')


if __name__ == '__main__':
    module = import_solution_module()
    s = module.S()
    s.solve()
    print(f'Part 1: {s.p1}')
    print(f'Part 2: {s.p2}')
    s.copy()
