# Problem_81
# Path sum: two ways
# In the 5 by 5 matrix below,
# """
# 131 673 234 103 18
# 201 96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524 37 331
# """
# the minimal path sum from the top left to the bottom right,
# by only moving to the right and down, is indicated in bold red and is equal to 2427.
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
# a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right
# by only moving right and down.
import time

start_time = time.time()

with open('problem_81.txt', 'r') as f:
    matrix = [[int(n) for n in row.split(',')] for row in f.read().strip().split('\n')]

for i in range(len(matrix) - 2, -1, -1):
    matrix[i][len(matrix)-1] += matrix[i+1][len(matrix)-1]
    matrix[len(matrix)-1][i] += matrix[len(matrix)-1][i+1]

for j in range(len(matrix) - 2, -1, -1):
    for k in range(len(matrix) -2, -1, -1):
        matrix[j][k] += min(matrix[j][k+1], matrix[j+1][k])

print(matrix[0][0])
print("%.6f seconds" % (time.time() - start_time))
