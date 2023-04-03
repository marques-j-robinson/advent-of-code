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

## Solving Puzzles
If there is no year directory in the `Events/` directory, then one must be created.
Same goes for the day.

The below snippet handles this for *event*=**2015** and *day*=**01**:
```bash
mkdir Events/2015 && touch Events/2015/day01.py
```

Start the main solution wrapper script by executing `main.py`. Execute `python main.py --help` for documentation.

The below snippet is an example of solving the first puzzle from [the website](https://adventofcode.com/2015/day/1).
```bash
python main.py -e 2015 -d 1
```

## Cache Layer
Before requesting `puzzle_input` there is a check to confirm that the puzzle input can not be found in the `cache` directory.

## Requesting puzzle input from the Advent of Code server
- `python-dotenv` keeps track of an individuals cookie
- `urllib3` make the request to the Advent of Code server
- The response to a successful request is formatted as the initial puzzle input 

## Expected Errors and Troubleshooting
This section is to help with identifiying and consolidating issues with this repository.

### No Cache Directory
**Log Example:** `FileNotFoundError: [Errno 2] No such file or directory: 'cache/2015_01'`
**Fix:** Create the `cache/` directory at the root of this repository. *Note: This directory will be ignored by version control*

```bash
mkdir cache
```

### No Events Directory
**Log Example:** `ModuleNotFoundError: No module named 'Events'`
**Fix:** Create the `Events/` directory at the root of this repository.

```bash
mkdir Events
```

### No Year/Event Directory
**Log Example:** `ModuleNotFoundError: No module named 'Events.2015'`
**Fix:** Create the `Events/2015/` directory.

```bash
mkdir Events/2015
```

### No Solution File
**Log Example:** `ModuleNotFoundError: No module named 'Events.2015.day01'`
**Fix:** Create the `Events/2015/day01.py` file.

```bash
touch Events/2015/day01.py
```

### All Files Exist, but Solution File is Empty
**Log Example:** `AttributeError: module 'Events.2015.day01' has no attribute 'S'`
**Fix:** Execute the main wrapper script. A built in feature of this script is creating
the directories and files needed to exit the program without any errors

```bash
python main.py -y 2015 -d 1
```