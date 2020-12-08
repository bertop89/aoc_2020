with open("input.txt", 'r') as file:
    input = [[line.split(" ")[0], int(line.split(" ")[1])] for line in file.readlines()]


def parse_program(input):
    i = acc = 0
    visited = set()
    while True:
        if i in visited:
            return False, acc
        visited.add(i)
        operation, operand = input[i]
        if operation == 'acc':
            acc += operand
            i += 1
        elif operation == 'jmp':
            i += operand
        elif operation == 'nop':
            i += 1
        if i == len(input):
            return True, acc

status, acc = parse_program(input)
print(acc)

import copy
for i in range(len(input)):
    copied_input = copy.deepcopy(input)
    current_op = copied_input[i][0]
    if current_op == 'jmp':
        copied_input[i][0] = 'nop'
    elif current_op == 'nop':
        copied_input[i][0] = 'jmp'
    else:
        continue
    status, acc = parse_program(copied_input)
    if status:
        print(acc)
