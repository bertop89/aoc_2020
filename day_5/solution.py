import math


def binary_space_partition(line, size):
    left = 0
    right = size
    for char in line:
        if char == 'F' or char == 'L':
            right = right - math.ceil((right-left)/2)
            res = left
        elif char == 'B' or char == 'R':
            left = left + math.ceil((right-left)/2)
            res = right
    return res

seat_ids = []
with open("input.txt", 'r') as file:
    for line in file:
        row = binary_space_partition(line[:7], 127)
        col = binary_space_partition(line[7:], 7)
        seat_id = row*8 + col
        seat_ids.append(seat_id)

print(set(range(min(seat_ids), max((seat_ids))))-set(seat_ids))
print(max(seat_ids))
