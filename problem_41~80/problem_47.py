# Problem_47
# Distinct primes factors
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?

import time

start_time = time.time()

primes = [n for n in range(2*10**5)]
primes[1] = 0
for i in range(2, len(primes)):
    if primes[i] != 0:
        for j in range(i*2, len(primes), i):
            primes[j] = 0

primes = set(n for n in primes if n != 0)

def get_prime_factors(n):
    factors = set()
    last_divisor = 0
    for d in range(2, int(n**0.5) + 1):
        while n % d == 0:
            factors.add(d)
            n //= d
        if n in primes:
            factors.add(n)
            break
    return factors

n = 1
consecutive = 0
while consecutive != 4:
    if len(get_prime_factors(n)) == 4:
        consecutive += 1
    else:
        consecutive = 0
    n += 1
print(n - 4)
print("%.6f seconds" % (time.time() - start_time))

# reference
# t2 = time.time()
# nums = [0]*2*10**5
# for i in range(2, 2*10**5):
#     if nums[i] == 0:
#         for j in range(i, 2*10**5, i):
#             nums[j] += 1
# n = 0
# consecutive = 0
# while consecutive != 4:
#     if nums[n] == 4:
#         consecutive += 1
#     else:
#         consecutive = 0
#     n += 1
# print(n-4)
# print("%.6f seconds" % (time.time() - t2))
