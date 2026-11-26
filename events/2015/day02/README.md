# Day 2: I Was Told There Would Be No Math

Run solution by executing:

```bash
python -m events.2015.day02.solution
```

## Part 1

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length `l`, width `w`, and height `h`) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect [right rectangular prism](https://en.wikipedia.org/wiki/Rectangular_cuboid)), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is `2*l*w + 2*w*h + 2*h*l`. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

- A present with dimensions `2x3x4` requires `2*6 + 2*12 + 2\*8 = 52` square feet of wrapping paper plus `6` square feet of slack, for a total of `58` square feet.
- A present with dimensions `1x1x10` requires `2*1 + 2*10 + 2\*10 = 42` square feet of wrapping paper plus `1` square foot of slack, for a total of `43` square feet.

## Problem Statement

All numbers in the elves' list are in feet. How many total **square feet of wrapping paper** should they order?

## Algorithm

1. Keep track of total, starting at 0
1. Split the input data by new line
1. Loop through split input data
   - Extract `l`, `w`, `h` values by splitting by `x`
   - Calculate the surface area
   - Calculate the area of the smallest side
   - Add the results of these calculations to the total
1. After looping, the total is the answer

### Big O Notation

## Part 2

## Problem Statement

## Algorithm

### Big O Notation
