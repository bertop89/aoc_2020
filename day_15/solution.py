from collections import defaultdict

def compute_n_spoken_numbers(starting_numbers, n=2020):
    spoken_nums = defaultdict(list)
    i = 0
    for number in starting_numbers:
        spoken_nums[number].append(i)
        i += 1
    last_spoken = starting_numbers[-1]
    while i < n:
        current_spoken = spoken_nums.get(last_spoken, None)
        if current_spoken is None:
            last_spoken = 0
        else:
            if len(current_spoken) < 2:
                last_spoken = 0
            else:
                last_spoken = current_spoken[-1] - current_spoken[-2]
        spoken_nums[last_spoken].append(i)
        i += 1
    return last_spoken

# part 1
print(compute_n_spoken_numbers([10,16,6,0,1,17]))

# part 2
print(compute_n_spoken_numbers([10,16,6,0,1,17], n=30000000))
