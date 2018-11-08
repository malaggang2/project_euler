# Problem_77
# Prime summations
# It is possible to write ten as the sum of primes in exactly five different ways:
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
# What is the first value which can be written as the sum of primes in over five thousand different ways?

import time

start_time = time.time()

nums = [n for n in range(10**2)]
nums[1] = 0
for i in range(2, int(len(nums)**0.5)+1):
    if nums[i] != 0:
        for j in range(i*2, len(nums), i):
            nums[j] = 0

target = 10
while True:
    primes = [n for n in nums if n != 0 and n < target]
    ways = [1] + [0] * target
    for p in primes:
        for i in range(p, len(ways)):
            ways[i] += ways[i - p]
    if ways[-1] >= 5000:
        break
    target += 1

print(target)
print("%.6f seconds" % (time.time() - start_time))
