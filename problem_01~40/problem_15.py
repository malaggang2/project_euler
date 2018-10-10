# Problem_15
# Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

def search_road(a, b):
    i = 1
    num = [1] * b
    while i < a + 1:
        num[0] = num[0] + 1
        for j in range(1, b):
            num[j] = num[j] + num[j-1]
        i += 1
    return num[-1]

print(search_road(20, 20))

def search_road_by_matrix(a, b):
    matrix = [[1 for col in range(a+1)] for row in range(b+1)]
    for i in range(1, a+1):
        for j in range(1, b+1):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix[a][b]

print(search_road_by_matrix(20, 20))

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def num_of_road(a, b):
    denominator = factorial(a + b)
    numerator = factorial(a)*factorial(b)
    return int(denominator / numerator)

print(num_of_road(20, 20))
