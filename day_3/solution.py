import numpy as np

lines = []
with open("input.txt", 'r') as file:
    for line in file:
        lines.append(list(map(lambda x: 0 if x == '.' else 1, line[:-1])))


def traverse_mat(lines, right, down):
    orig_mat = np.array(lines)
    mat = orig_mat.copy()

    max_dim = max(right, down)

    while mat.shape[1] < mat.shape[0]*max_dim:
        mat = np.concatenate((mat, orig_mat), axis=1)

    count = i = j = 0
    while i+down < mat.shape[0] and j+right < mat.shape[1]:
        i += down
        j += right
        count += mat[i, j]

    return count


results = [
    traverse_mat(lines, 1, 1),
    traverse_mat(lines, 3, 1),
    traverse_mat(lines, 5, 1),
    traverse_mat(lines, 7, 1),
    traverse_mat(lines, 1, 2)
]

print(results[1])
print(np.prod(results))

