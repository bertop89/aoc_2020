import numpy as np
import itertools

cube_list = []
with open("input.txt", 'r') as file:
    for line in file.readlines():
        cube_list.append([1 if x == "#" else 0 for x in line[:-1]])
original_cube = np.array(cube_list)
print(original_cube.shape)



def get_neighbors(idx, mat, dims=3):
    neighbors = []
    for comb in itertools.product([-1,0,1], repeat=dims):
        new_idx = [x+y for x,y in zip(idx,comb)]
        if any(map(lambda x: x < 0, new_idx)) or all(map(lambda x: x == 0, comb)):
            continue
        try:
            if dims == 3:
                neighbors.append(mat[new_idx[0], new_idx[1], new_idx[2]])
            elif dims == 4:
                neighbors.append(mat[new_idx[0], new_idx[1], new_idx[2], new_idx[3]])
        except:
            pass
    return neighbors


# part 1

cube_mat = np.expand_dims(original_cube, axis=2)
cube_mat = np.pad(cube_mat, 6, mode='constant', constant_values=0)
print(cube_mat.shape)
for i in range(6):
    new_cube = cube_mat.copy()
    for idx, val in np.ndenumerate(cube_mat):
        neighbors = get_neighbors(idx, cube_mat)
        if val == 0:
            new_val = 1 if sum(neighbors) == 3 else 0
        elif val == 1:
            new_val = 1 if 2 <= sum(neighbors) <= 3 else 0
        new_cube[idx] = new_val
    cube_mat = new_cube
print(np.sum(cube_mat))

# part 2

cube_mat = np.expand_dims(original_cube, axis=2)
cube_mat = np.expand_dims(cube_mat, axis=3)
cube_mat = np.pad(cube_mat, 6, mode='constant', constant_values=0)
print(cube_mat.shape)
for i in range(6):
    new_cube = cube_mat.copy()
    for idx, val in np.ndenumerate(cube_mat):
        neighbors = get_neighbors(idx, cube_mat, dims=4)
        if val == 0:
            new_val = 1 if sum(neighbors) == 3 else 0
        elif val == 1:
            new_val = 1 if 2 <= sum(neighbors) <= 3 else 0
        new_cube[idx] = new_val
    cube_mat = new_cube
print(np.sum(cube_mat))
