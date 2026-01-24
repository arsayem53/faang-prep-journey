matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print(f"matrix[{i}][{j}] = {element}")

for row in matrix:
    row_sum = sum(row)  # Python's built-in sum()
    print(row_sum)

maximum = matrix[0][0]
for row in matrix:
    for element in row:
        if element > maximum:
            maximum = element
print("Maximum element in the matrix is:", maximum)