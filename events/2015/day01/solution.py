from lib.file_system import read_input_data

data = read_input_data('2015', 'day01')

floor = 0
basement_entered = False
for p, instruction in enumerate(data):
    if instruction == "(":
        floor+=1
    else:
        floor-=1
    if basement_entered == False and floor == -1:
        print(f"PART_2: Santa first enters the basement at position {p}")
        basement_entered = True
print(f"PART_1: Santa reaches floor {floor}")