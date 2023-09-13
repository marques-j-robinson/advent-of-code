import os
import argparse
import importlib
from shutil import copyfile

import urllib3
import pyperclip
from dotenv import load_dotenv
load_dotenv()


def get_event_day_by_puzzle_id(puzzle_id):
    """
    Provided a puzzle id `2015_01`, will return event as 2015 and day as 01
    Another example id `2017_22`, will return event as 2017 and day as 22
    """
    return [i for i in puzzle_id.split("_")]


def configure_puzzle_id():
    """
    Use command line arguments first, then look for
    values in the .env file and finally default to
    provided files in this function.
    """
    DEFAULT_EVENT = 2015
    DEFAULT_DAY = 1

    # Command Line Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--Event", help="Event ID")
    parser.add_argument("-d", "--Day", help="Day ID")
    args = parser.parse_args()

    event = args.Event or os.getenv("EVENT") or DEFAULT_EVENT
    day = args.Day or os.getenv("DAY") or DEFAULT_DAY
    day_with_leading_zero = str(day).zfill(2)
    return f"{event}_{day_with_leading_zero}"


def get_puzzle_input(puzzle_id):
    """
    Fetches input data using the configured event/day values.
    """
    print("Fetching puzzle input...")
    base_url = "https://adventofcode.com"
    [event, day] = get_event_day_by_puzzle_id(puzzle_id)
    puzzle_input_url = f"{base_url}/{event}/day/{int(day)}/input"
    request_headers = {"Cookie":f'session={os.getenv("TOKEN")}'}
    try:
        http = urllib3.PoolManager()
        response = http.request("GET", puzzle_input_url, headers=request_headers)
        return response.data.decode("utf-8").rstrip("\n")
    except Exception as e:
        print("Exception thrown while fetching puzzle input!!")
        print(e)
        print("Please remember to configure the .env file with a useful TOKEN value.")


def import_solution_module(puzzle_id, puzzle_input):
    """
    Uses importlib with the event/day values return the correct solution module.
    """
    [event, day] = get_event_day_by_puzzle_id(puzzle_id)
    try:
        solution_module = importlib.import_module(f"Events.{event}.day{day}")
        return solution_module.Solution(puzzle_input)
    except Exception as e:
        print("Exception thrown during module import!!")
        print(e)
        print("Please remember to create the Event folder as well as the solution module and class.")


def copy_solution_template(puzzle_id):
    [event, day] = get_event_day_by_puzzle_id(puzzle_id)
    filename = f'Events/{event}/day{day}.py'
    if os.path.exists(filename):
        print(f'{event}_{day} PUZZLE ALREADY GENERATED!')
    else:
        copyfile('template.py', filename)
        print(f'Generated puzzle at {filename}')


if __name__ == "__main__":
    puzzle_id = configure_puzzle_id()
    print(f"Executing {puzzle_id} Solution...")
    copy_solution_template(puzzle_id)
    puzzle_input = get_puzzle_input(puzzle_id)
    s = import_solution_module(puzzle_id, puzzle_input)
    s.solve()
    print(f"Part 1: {s.p1}")
    if s.p2 == 0:
        pyperclip.copy(str(s.p1))
    else:
        print(f"Part 2: {s.p2}")
        pyperclip.copy(str(s.p2))
