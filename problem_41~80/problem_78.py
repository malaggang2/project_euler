# Problem_78
# Coin partitions
# Let p(n) represent the number of different ways in which n coins can be
# separated into piles.
# For example, five coins can be separated into piles in exactly seven different ways,
# so p(5)=7.
#
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n for which p(n) is divisible by one million.

import time

start_time = time.time()

pentagonals = sum([[int(n*(3*n - 1)/2), int(n*(3*n + 1)/2)] for n in range(1, 250)], [])

partitions = [1]
sign = [1, 1, -1, -1]
n = 0
while partitions[n] != 0:
    n += 1
    p = 0
    i = 0
    while n >= pentagonals[i]:
        p += partitions[n - pentagonals[i]] * sign[i%4]
        i += 1
    partitions.append(p % 10**6)

print(n)
print("%.6f seconds" % (time.time() - start_time))
