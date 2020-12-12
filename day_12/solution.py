import math

with open("input.txt", 'r') as file:
    original_input = [(line[0], int(line[1:-1])) for line in file.readlines()]

x = y = 0
dir = 1
dir_to_vect = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0)
}

# part 1
for row in original_input:
    inst, value = row
    if inst == 'N':
        y += value
    elif inst == 'S':
        y -= value
    elif inst == 'E':
        x += value
    elif inst == 'W':
        x -= value
    elif inst == 'L':
        dir = (dir - (value // 90)) % 4
    elif inst == 'R':
        dir = (dir + (value // 90)) % 4
    elif inst == 'F':
        vect_x, vect_y = dir_to_vect[dir]
        x += vect_x*value
        y += vect_y*value

print((x, y))
print(abs(x)+abs(y))

# part 2
x_w = 10
y_w = 1
x_s = y_s = 0


def rotate(x, y, xo, yo, theta):
    xr = math.cos(theta)*(x-xo)-math.sin(theta)*(y-yo) + xo
    yr = math.sin(theta)*(x-xo)+math.cos(theta)*(y-yo) + yo
    return [round(xr), round(yr)]


for row in original_input:
    inst, value = row
    if inst == 'N':
        y_w += value
    elif inst == 'S':
        y_w -= value
    elif inst == 'E':
        x_w += value
    elif inst == 'W':
        x_w -= value
    elif inst == 'L':
        x_w, y_w = rotate(x_w, y_w, 0, 0, math.radians(value))
    elif inst == 'R':
        x_w, y_w = rotate(x_w, y_w, 0, 0, -math.radians(value))
    elif inst == 'F':
        x_s += x_w*value
        y_s += y_w*value

print((x_s, y_s))
print(abs(x_s)+abs(y_s))
