from collections import Counter

with open("input.txt", 'r') as file:
    input = [int(line) for line in file.readlines()]

# part 1
device_jolt = max(input) + 3
print(device_jolt)

input_sorted = sorted(input)
input_sorted.insert(0, 0)
input_sorted.append(device_jolt)

joltage_diffs = [y-x for x, y in zip(input_sorted, input_sorted[1:])]
counter = Counter(joltage_diffs)
print(counter[1]*counter[3])


# part 2
candidates = [0]
elements = set(input_sorted)

memo = {}


def recursive_lookup(current_element):
    counter = 0
    if current_element in memo:
        return memo[current_element]
    for i in range(1, 4):
        new_element = current_element + i
        if new_element == device_jolt:
            counter += 1
        elif new_element in elements:
            counter += recursive_lookup(new_element)
    memo[current_element] = counter
    return counter


print(recursive_lookup(0))

