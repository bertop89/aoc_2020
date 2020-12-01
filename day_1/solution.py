from itertools import combinations
from functools import reduce

numbers = []
with open("input.txt", 'r') as file:
    for line in file:
        numbers.append(int(line))


def find_and_multiply(numbers, size):
    for comb in combinations(numbers, size):
        if sum(comb) == 2020:
            return reduce((lambda x, y: x * y), comb)


print(find_and_multiply(numbers, 2))

print(find_and_multiply(numbers, 3))
