
any_count = all_count = 0
any_group = set()
all_group = set()
start_group = True
with open("input.txt", 'r') as file:
    for line in file:
        if line == '\n':
            any_count += len(any_group)
            all_count += len(all_group)
            any_group = set()
            all_group = set()
            start_group = True
        else:
            current_group = set(line[:-1])
            any_group = any_group.union(current_group)
            if start_group:
                all_group = current_group
                start_group = False
            else:
                all_group = all_group.intersection(current_group)
any_count += len(any_group)
print(any_count)

all_count += len(all_group)
print(all_count)
