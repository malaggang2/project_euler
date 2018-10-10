# Problem_35
# Circular primes
#
# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

import time

start_time = time.time()

nums = [n for n in range(10**6)]
nums[1] = 0
for i in range(2, int(len(nums)**0.5)+1):
    for j in range(i*2, len(nums), i):
        nums[j] = 0

primes = [num for num in nums if num != 0]
circular_primes = []
for prime in primes:
    if prime in circular_primes:
        continue
    prime = str(prime)
    tmp = [int(prime[i:]+prime[:i]) for i in range(len(prime))]
    if len([1 for x in tmp if nums[x] == 0]) > 0:
        continue
    circular_primes += list(set(tmp))

print(len(circular_primes))
print('%.6f seconds' % (time.time()-start_time))

# # itertools 활용
# import itertools
#
# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
#
# answer = 2
# for digit in range(1, 7):
#     for num in itertools.product('1379', repeat=digit):
#         for circle in range(len(num)):
#             if not is_prime(int(''.join(num[circle:]+num[:circle]))):
#                 break
#         else:
#             answer += 1
# print(answer)
