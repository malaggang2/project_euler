# Problem_49
# Prime Permutations
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

import time
from itertools import permutations, combinations, combinations_with_replacement
from statistics import mean

start_time = time.time()
nums = [n for n in range(10**4)]
nums[1] = 0
for i in range(2, len(nums)):
    if nums[i] != 0:
        for j in range(i*2, len(nums), i):
            nums[j] = 0
primes = set(n for n in nums if n != 0)

result = []
for i in combinations_with_replacement('1234567890', 4):
    primes_set = set()
    for j in permutations(i):
        num = ''.join(j)
        if int(num) > 10**3 and int(num) in primes:
            primes_set.add(int(num))
    for s in combinations(primes_set, 3):
        sequences = set(n for n in s)
        if mean(sequences) in sequences:
            result.append(''.join([str(n) for n in sequences]))
print(result)
print("%.6f seconds" % (time.time() - start_time))
