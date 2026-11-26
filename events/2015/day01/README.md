# Day 1: Not Quite Lisp

Run solution by executing:

```bash
python events/2015/day01/solution.py
```

## Part 1

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor `0`) and then follows the instructions one character at a time.

An opening parenthesis, `(`, means he should go up one floor, and a closing parenthesis, `)`, means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

```
(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
```

### Problem Statement

To **what floor** do the instructions take Santa?

### Algorithm

1. Keep track of floor, starting at 0
1. Loop through puzzle input
   - Based on value from puzzle input, increase or decrease floor
1. Final floor is the answer

### Big O

- Time: O(n)
- Space: O(1)

## Part 2

Now, given the same instructions, find the **position** of the first character that causes him to enter the basement (floor `-1`). The first character in the instructions has position `1`, the second character has position `2`, and so on.

For example:

```
) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
```

### Problem Statement

What is the **position** of the character that causes Santa to first enter the basement?

### Algorithm

1. Keep track of floor, starting at 0
1. Keep track of whether the basement has been entered, starting as `false`
1. Loop through puzzle input
   - Based on value from puzzle input, increase or decrease floor
   - When the floor is `-1` and the basement entry is `false`
     - Update basement entry to `true`
     - The **position** is the answer

### Big O

- Time: O(n)
- Space: O(1)
