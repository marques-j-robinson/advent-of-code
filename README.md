# Advent of Code
Wrapper script for managing solutions to [this website](https://adventofcode.com/) written in Python.

## Startup
After cloning (master) for the very first time:
```bash
$ cp .template-env .env && mkdir cache && mkdir Events
# The command above does three things:
# 1) Copies /.template-env to /.env within the root of this project
# 2) Creates a directory named cache (Note: This directory will be ignored by version control)
# 3) Creates an additional directory named Events
```

Setup Development Environment:
```bash
# Create a virtual environment
$ python -m venv venv
# Activate the virtual environment (Windows: .\venv\Scripts\activate)
$ source venv/bin/activate
# Install requirements
(venv) $ pip install -r requirements.txt
```

Start the main solution wrapper script by executing `main.py`. Execute `python main.py --help` for documentation.
Below is an example of solving the first solution from the website.
```bash
# Start server with very first puzzle paramerters
(venv) $ python main.py -e 2015 -d 1
```

## Cache Layer
Before requesting `puzzle_input` there is a check to confirm that the puzzle input can not be found in the `cache` directory.

## Requesting puzzle input from the Advent of Code server
- `python-dotenv` keeps track of an individuals cookie
- `urllib3` make the request to the Advent of Code server
- The response to a successful request is formatted as the initial puzzle input 