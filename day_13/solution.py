with open("input.txt", 'r') as file:
    timestamp = int(file.readline()[:-1])
    raw_ids = file.readline().split(",")

# part 1
bus_ids = [int(x) for x in raw_ids if x != 'x']
print(timestamp)
print(bus_ids)

possible_ids = []
for id in bus_ids:
    current = 0
    while current <= timestamp:
        current += id
    possible_ids.append(current)
print((min(possible_ids) - timestamp)*bus_ids[possible_ids.index(min(possible_ids))])

# part 2
index_ids = [raw_ids.index(x) for x in raw_ids if x != 'x']
index_str = str(index_ids[1:])
print(index_ids)

i = mult = 1
step_value = bus_ids[0]
id = bus_ids[0]
while True:
    id = id + step_value
    while i < len(index_ids):
        offset = index_ids[i]
        if ((id + offset) % bus_ids[i]) == 0:
            step_value = step_value * bus_ids[i]
            i += 1
        else:
            mult += 1
        break
    if i >= len(index_ids):
        print(id)
        break
