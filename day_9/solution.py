from itertools import combinations

with open("input.txt", 'r') as file:
    input = [int(line) for line in file.readlines()]


def compute_sums(input):
    return [sum(x) for x in combinations(input, 2)]


def compute_invalid_number(input, preamble=25):
    i = preamble
    while i<len(input):
        current_sums = (compute_sums(input[i-preamble:i]))
        if input[i] not in current_sums:
            return input[i]
        i += 1
    return None

invalid_number = compute_invalid_number(input)
print(invalid_number)

def compute_weakness(input, invalid_number):
    for subset in [input[i:i+j] for i in range(0,len(input)) for j in range(1,len(input)-i+1)]:
        if sum(subset) == invalid_number:
            return min(subset) + max(subset)

print(compute_weakness(input, invalid_number))

