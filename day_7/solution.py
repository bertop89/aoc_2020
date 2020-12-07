bags_dict = {}
with open("input.txt", 'r') as file:
    for line in file:
        key, values = [x.replace("bags", "").replace("bag", "").strip() for x in line.split("contain")]
        if "no other" in values:
            values = []
        else:
            values = [(x.replace(".", "").strip()[2:], int(x.strip()[0])) for x in values.split(',')]
        bags_dict[key] = values


def find_bag(bags_dict, current_bag, bag_to_find):
    count = 0
    for bag in current_bag:
        if bag[0] == bag_to_find:
            count +=1
        else:
            count += find_bag(bags_dict, bags_dict[bag[0]], bag_to_find)
    return count


count = 0
for key, value in bags_dict.items():
    count += int(find_bag(bags_dict, value, 'shiny gold') > 0)
print(count)


def find_bag_number(bags_dict, current_bag):
    count = 0
    for bag in current_bag:
        count += bag[1] + bag[1]*find_bag_number(bags_dict, bags_dict[bag[0]])
    return count


count = 0
for bag in bags_dict['shiny gold']:
    count += bag[1] + bag[1]*find_bag_number(bags_dict, bags_dict[bag[0]])
print(count)
