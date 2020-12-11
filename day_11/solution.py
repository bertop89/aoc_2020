input_lists = []
mapping_dict = {"L": 0, "#": 1, ".": -1}

with open("input.txt", 'r') as file:
    original_input = [[mapping_dict[char] for char in line if char != '\n'] for line in file.readlines()]

# part 1

idx_to_check = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]


def get_adjacent_count(input, row, col):
    result = []
    for idx_row, idx_col in idx_to_check:
        try:
            if row+idx_row >= 0 and col+idx_col >= 0 and input[row+idx_row][col+idx_col] == 1:
                result.append(True)
        except:
            pass
    return sum(result)


from copy import deepcopy


def proccess_round(input, threshold=4, fn=get_adjacent_count):
    new_input = deepcopy(input)
    for i in range(len(input)):
        for j in range(len(input[i])):
            count = fn(input, i, j)
            if input[i][j] == 0 and count == 0:
                new_input[i][j] = 1
            elif input[i][j] == 1 and count >= threshold:
                new_input[i][j] = 0
    return new_input

input = deepcopy(original_input)
while True:
    new_input = proccess_round(input)
    if new_input == input:
        break
    input = new_input

print(new_input)
print(sum([sum([cell == 1 for cell in row]) for row in new_input]))

# part 2

def get_adjacent_count_long(input, row, col):
    result = []
    for idx_row, idx_col in idx_to_check:
        current_row = row + idx_row
        current_col = col + idx_col
        while current_row >= 0 and current_row < len(input) and current_col >= 0 and current_col < len(input[current_row]):
            if input[current_row][current_col] == 1:
                result.append(True)
                break
            elif input[current_row][current_col] == 0:
                break
            current_row += idx_row
            current_col += idx_col
    return sum(result)


input = deepcopy(original_input)
while True:
    new_input = proccess_round(input, threshold=5, fn=get_adjacent_count_long)
    if new_input == input:
        break
    input = new_input
print(new_input)
print(sum([sum([cell == 1 for cell in row]) for row in new_input]))
