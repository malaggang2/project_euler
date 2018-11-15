# Problem_83
# Path sum: four ways
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
# by moving left, right, up, and down, is indicated in bold red and is equal to 2297.
# """
# 131 673 234 103 18
# 201 96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524 37 331
# """
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
# a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right
# by moving left, right, up, and down.

import time

with open('problem_81.txt', 'r') as f:
    matrix = [[int(x) for x in row.split(',')] for row in f.read().strip().split('\n')]

n, m = len(matrix), len(matrix[0])

moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
graph = {}
for i in range(n):
    for j in range(m):
        adjacents = [(i+x, j+y) for x, y in moves if 0 <= (i+x) < n and 0 <= (j+y) < m]
        graph[(i, j)] = {(x, y):matrix[x][y] for (x, y) in adjacents}

start_time = time.time()

def dijkstra(source, start):
    distances = {vertex:float('inf') for vertex in source.keys()}
    x, y = start
    distances[start] = matrix[x][y]

    tmp = {start}

    while tmp:
        current_vertex = min(tmp, key=lambda x:distances[x])
        for adjacent, weigh in source[current_vertex].items():
            distance = distances[current_vertex] + weigh
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                tmp.add(adjacent)
        tmp.remove(current_vertex)
    return distances
print(dijkstra(graph, (0, 0))[(79, 79)])
print("%.6f seconds" % (time.time() - start_time))
