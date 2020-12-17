# part 1
valid_nums = set()
invalid_nums = list()
valid_tickets = list()
fields_dict = dict()
with open("input.txt", 'r') as file:
    ticket_mode = False
    for line in file.readlines():
        line = line[:-1]
        if line == '':
            continue
        if 'ticket' in line:
            ticket_mode = True
        elif not ticket_mode:
            field_key, ranges = line.split(":")
            ranges = ranges.split(" or ")
            total_range = set()
            for current_range in ranges:
                start, end = [int(x) for x in current_range.split("-")]
                total_range = total_range.union(set(range(start, end+1)))
            valid_nums = valid_nums.union(total_range)
            fields_dict[field_key] = total_range
        else:
            field_list = [int(x) for x in line.split(",")]
            current_invalid = list(set(field_list).difference(valid_nums))
            invalid_nums += current_invalid
            if len(current_invalid) == 0:
                valid_tickets.append(field_list)
print(sum(invalid_nums))

# part 2
my_ticket = valid_tickets[0]
nearby_valid_tickets = valid_tickets[1:]
from collections import defaultdict
candidates = defaultdict(list)

# collects all posible combinations
fields = fields_dict.keys()
for key, current_range in fields_dict.items():
    for j in range(len(fields)):
        field_values = set([x[j] for x in nearby_valid_tickets])
        if len(set(field_values).difference(current_range)) == 0:
            candidates[key].append(j)
#print({key: len(value) for key, value in candidates.items()})

# resolve combinations from more to less restrictive
final_result = dict()
while len(final_result.keys()) < len(fields):
    candidates_to_remove = [(key, value[0]) for key, value in candidates.items() if len(value) == 1]
    for candidate_field, candidate_pos in candidates_to_remove:
        final_result[candidate_field] = candidate_pos
        del candidates[candidate_field]
        candidates = {key: ([x for x in value if x!=candidate_pos] if candidate_pos in value else value) for key, value in candidates.items()}

from functools import reduce
#print(final_result)
departures = [value for key, value in final_result.items() if key.startswith("departure")]
#print(departures)
#print(my_ticket)
print(reduce((lambda x, y: x * y), [my_ticket[x] for x in departures]))


