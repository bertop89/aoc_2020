# part 1
mem = dict()
with open("input.txt", 'r') as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        if line[:4] == 'mask':
            current_mask = line.split(" = ")[1]
        else:
            pos = int(line[line.find("[")+1:line.find("]")])
            value = int(line.split(" = ")[1])
            value_bin = format(value, "b").zfill(36)
            result = [x if y =='X' else y for x, y in zip(value_bin, current_mask)]
            mem[pos] = int(''.join(result), 2)
print(sum(mem.values()))

# part 2
import math
def generate_floatings(input):
    combs = math.pow(2, sum([x == 'X' for x in input]))
    stack = [input]
    while len(stack) < combs:
        current = stack.pop(0)
        idx = current.find('X')
        if idx == -1:
            stack.append(current)
        else:
            stack.append(current[0:idx]+'1'+current[idx+1:])
            stack.append(current[0:idx]+'0'+current[idx+1:])
    return stack


mem = dict()
with open("input.txt", 'r') as file:
    for line in file.readlines():
        line = line.replace("\n", "")
        if line[:4] == 'mask':
            current_mask = line.split(" = ")[1]
        else:
            pos = int(line[line.find("[")+1:line.find("]")])
            value = int(line.split(" = ")[1])
            pos_bin = format(pos, "b").zfill(36)
            pos_result = [x if y == '0' else y for x, y in zip(pos_bin, current_mask)]
            positions = generate_floatings(''.join(pos_result).lstrip('0'))
            for pos in positions:
                mem[int(pos, 2)] = value
print(sum(mem.values()))
