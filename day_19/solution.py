rules = dict()
with open("input.txt", 'r') as file:
    line = file.readline()
    while line != '\n':
        key, value = line[:-1].split(':')
        rules[key] = [x.strip().split(' ') for x in value.replace("\"", "").strip().split('|')]
        line = file.readline()

    test = set([x[:-1] for x in file.readlines()])

def generate_cases(rules, test_cases):
    test_cases = set(test_cases)
    found_cases = list()
    for case in test_cases:
        candidates_queue = [(['0'], '')]
        while len(candidates_queue) > 0:
            current_candidate = candidates_queue.pop()
            if current_candidate[1] == case and len(current_candidate[0]) == 0:
                found_cases.append(current_candidate[1])
                break
            if len(current_candidate[0]) > 0:
                for new_candidate in rules[current_candidate[0][0]]:
                    if new_candidate[0] not in rules.keys():
                        if case.startswith(current_candidate[1]+new_candidate[0]):
                            candidates_queue.append((current_candidate[0][1:], (current_candidate[1]+new_candidate[0])))
                    else:
                        candidates_queue.append((new_candidate + current_candidate[0][1:], current_candidate[1]))
    return found_cases


# part 1
candidates = generate_cases(rules, test)
print(len(candidates))

# part 2
max_rec = 10
rules['8'] = [['42']*i for i in range(1, max_rec)]
rules['11'] = [['42']*i+['31']*i for i in range(1, max_rec)]
candidates = generate_cases(rules, test)
print(len(candidates))
