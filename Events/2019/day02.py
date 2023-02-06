from format_data import split_by_comma, int_list


def format_puzzle_input(puzzle_input):
    return int_list(split_by_comma(puzzle_input))


def p1(puzzle_input):
    puzzle_input = format_puzzle_input(puzzle_input)
    puzzle_input[1] = 12
    puzzle_input[2] = 2
    idx = 0
    addcode = 1
    multiplycode = 2
    exitcode = 99
    step = 4
    while idx < len(puzzle_input):
        opcode = puzzle_input[idx]
        if opcode == exitcode:
            break
        a = puzzle_input[idx+1]
        b = puzzle_input[idx+2]
        c = puzzle_input[idx+3]
        if opcode == addcode:
            puzzle_input[c] = puzzle_input[a]+puzzle_input[b]
        if opcode == multiplycode:
            puzzle_input[c] = puzzle_input[a]*puzzle_input[b]
        idx += step
    print(puzzle_input)
    return puzzle_input[0]


def p2(puzzle_input):
    res = 0
    puzzle_input = format_puzzle_input(puzzle_input)
    return res
