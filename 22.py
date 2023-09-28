# Matrix
import copy

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])

copy1 = copy.copy(matrix)
copy1[0] = [3, 2, 1]
print(matrix)
print(copy1)

copy2 = copy.copy(matrix)
copy2[0][1] = 7
print(matrix)
print(copy2)

copy3 = copy.deepcopy(matrix)
copy3[0][2] = 1
print(matrix)
print(copy3)
