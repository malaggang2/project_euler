# Problem_67
# Maximum path sum II
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and
# 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18.
# It is not possible to try every route to solve this problem, as there are 299 altogether!
# If you could check one trillion (1012) routes every second it would take over
# twenty billion years to check them all.
# There is an efficient algorithm to solve it. ;o)

import time

start_time = time.time()
with open('problem_67.txt', 'r') as f:
    data = [[int(x) for x in n.split(' ')] for n in f.read().strip().split('\n')]

for i in range(len(data) - 2, -1, -1):
    for j in range(i, -1, -1):
        data[i][j] += max(data[i+1][j], data[i+1][j+1])
print(data[0][0])
print("%.6f seconds" % (time.time() - start_time))
