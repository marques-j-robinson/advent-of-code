# My aoc Solutions
Solutions to [aoc](https://adventofcode.com/).

## Setup
- clone repo
- Create Virtial Environment: `python -m venv venv && source venv/bin/activate`
- Install Dependencies: `pip install --upgrade pip && pip install -r requirements.txt`

**Tip** Recieving permission denied error while piping stored puzzle input file to node script? Following these for [basic chmod usage](https://stackoverflow.com/a/48757287) and [-R flag usage](https://stackoverflow.com/a/11512211)

```bin
sudo chmod -R 755 cache/
```

## Download Script
Python script that stores puzzle input files to the filesystem.

**Notes**
- *Event* and *Day* are configurable within `download.py`
- Ensure virtual environment is active and dependencies installed

```bin
python download.py
```
