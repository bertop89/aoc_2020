from collections import defaultdict

with open("input.txt", 'r') as file:
    input = [line[:-1] for line in file.readlines()]

def get_coord_from_line(line):
    x = y = 0
    i = 0
    while i < len(line):
        coord = line[i]
        if (coord == 'n' or coord == 's') and (line[i + 1] == 'w' or line[i + 1] == 'e'):
            coord += line[i + 1]
            i += 1
        if coord == 'w':
            x -= 1
        elif coord == 'e':
            x += 1
        elif len(coord) == 2:
            if coord[0] == 'n':
                y += 1
            else:
                y -= 1
            if coord[1] == 'w':
                x -= 0.5
            else:
                x += 0.5
        i += 1
    return x, y

# part 1
tile_dict = defaultdict(lambda: 0)
for line in input:
    x, y = get_coord_from_line(line)
    tile_dict[x,y] = 1 if tile_dict[x,y] == 0 else 0
print(sum(value == 0 for value in tile_dict.values()))
print(sum(value == 1 for value in tile_dict.values()))

# part 2
def get_adjacent_tiles(x,y):
    return [
        (x-1, y),
        (x+1, y),
        (x-0.5, y+1),
        (x+0.5, y+1),
        (x-0.5, y-1),
        (x+0.5, y-1)
    ]
def get_adjacent_black_tile(tile_dict, x, y):
    result = [tile_dict.get((x,y)) for x, y in get_adjacent_tiles(x,y)]
    return sum(value == 1 for value in result)


tile_dict = defaultdict(lambda: 0)
for day in range(1, 101):
    if day == 1:
        for line in input:
            x, y = get_coord_from_line(line)
            tile_dict[x, y] = 1 if tile_dict[x, y] == 0 else 0
    tiles_to_check = list(tile_dict.keys())
    adjacent_tiles = [get_adjacent_tiles(x,y) for (x,y),value in tile_dict.items() if value == 1]
    tiles_to_check = set(tiles_to_check + [item for items in adjacent_tiles for item in items])
    temp_tile_dict = defaultdict(lambda: 0)
    for x,y in tiles_to_check:
        num_black_adj = get_adjacent_black_tile(tile_dict, x, y)
        if tile_dict[x,y] == 1 and (num_black_adj == 0 or num_black_adj > 2):
            temp_tile_dict[x,y] = 0
        elif tile_dict[x,y] == 0 and num_black_adj == 2:
            temp_tile_dict[x,y] = 1
        else:
            temp_tile_dict[x, y] = tile_dict[x,y]
    tile_dict = temp_tile_dict.copy()
    print(f"Day {day}: {sum(value == 1 for value in tile_dict.values())}")
