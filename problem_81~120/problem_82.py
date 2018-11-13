# Problem_82
# Path sum: three ways
# The minimal path sum in the 5 by 5 matrix below, by starting in any cell
# in the left column and finishing in any cell in the right column, and only moving
# up, down, and right, is indicated in red and bold; the sum is equal to 994.
# """
# 131 673 234 103 18
# 201 96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524 37 331
# """
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
# a 31K text file containing a 80 by 80 matrix, from the left column to the right column.
import time

start_time = time.time()

with open('problem_81.txt', 'r') as f:
    matrix = [[int(n) for n in row.split(',')] for row in f.read().strip().split('\n')]

n, m = len(matrix), len(matrix[0])

pathsum = [matrix[i][-1] for i in range(n)]

for i in range(m-2, -1, -1):
    pathsum[0] += matrix[0][i]
    for j in range(1, n):
        pathsum[j] = min(pathsum[j], pathsum[j-1]) + matrix[j][i]
    for p in range(m-2, -1, -1):
        pathsum[p] = min(pathsum[p], pathsum[p+1] + matrix[p][i])

print(min(pathsum))
print("%.6f seconds" % (time.time() - start_time))
