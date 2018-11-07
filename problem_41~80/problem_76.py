# Problem_76
# Counting summations
# It is possible to write five as a sum in exactly six different ways:
#
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum of at least two positive integers?

import time

start_time = time.time()

target = 100
ways = [1] + [0] * target

for num in range(1, target):
    for i in range(num, len(ways)):
        ways[i] += ways[i - num]
print(ways[-1])
print("%.6f seconds" % (time.time() - start_time))
