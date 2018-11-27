# Problem_91
# Right triangles with integer coordinates

# import time
# from itertools import product
#
# start_time = time.time()
# answer = 0
# for p in product(range(51), repeat=2):
#     for q in product(range(51), repeat=2):
#         x1, y1 = p
#         x2, y2 = q
#         op = x1**2 + y1**2
#         oq = x2**2 + y2**2
#         pq = (x2 - x1)**2 + (y2 - y1)**2
#         if op == 0 or oq == 0 or pq == 0:
#             continue
#         if op == oq + pq or oq == op + pq or pq == op + oq:
#             answer += 1
# print(int(answer/2))
# print('%.6f seconds' % (time.time() - start_time))

import time
from math import gcd

start_time = time.time()
count = 0
for x in range(1, 51):
    for y in range(1, 51):
        m = gcd(x, y)
        count += min(m*(50 - x)//y, m*y//x)
print(50*50*3 + count*2)
print('%.6f seconds' % (time.time() - start_time))
