parent_file_path = 'events/2015/day01/'

with open(f'{parent_file_path}data', 'r', encoding='utf-8') as file:
    data = file.read()

f = 0
for instruction in data:
    if instruction == "(":
        f+=1
    else:
        f-=1
print(f"PART_1: Santa reaches the {f} floor")