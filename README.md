# Advent of Code
Wrapper script for managing solutions to [this website](https://adventofcode.com/) written in Python.

## Startup
After cloning *master* for the very first time:
```bash
cp .template-env .env && mkdir cache && mkdir Events
# The command above does three things:
# 1) Copies /.template-env to /.env within the root of this project
# 2) Creates a directory named cache (Note: This directory will be ignored by version control)
# 3) Creates an additional directory named Events
```

Setup Development Environment:
```bash
python -m venv venv && source venv/bin/activate
# The command above does two things:
# 1) Creates a virtual environment
# 2) Activates the virtual environment (Windows: .\venv\Scripts\activate)
```

Install Dependencies:
```bash
pip install --upgrade pip && pip install -r requirements.txt
```

Start the main solution wrapper script by executing `main.py`. Execute `python main.py --help` for documentation.
Below is an example of solving the first solution from the website.
```bash
python main.py -e 2015 -d 1
# Start server with very first puzzle paramerters
```

## Cache Layer
Before requesting `puzzle_input` there is a check to confirm that the puzzle input can not be found in the `cache` directory.

## Requesting puzzle input from the Advent of Code server
- `python-dotenv` keeps track of an individuals cookie
- `urllib3` make the request to the Advent of Code server
- The response to a successful request is formatted as the initial puzzle input 
