# Problem_50
# Consecutive prime sum
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
import time

start_time = time.time()

nums = [n for n in range(10**6)]
nums[1] = 0
for i in range(2, int(len(nums)**0.5) + 1):
    if nums[i] != 0:
        for j in range(i*2, len(nums), i):
            nums[j] = 0
primes = [n for n in nums if n != 0]
primes_set = set(primes)

answer = 0
longest_length = 0
for i in range(len(primes)):
    sum_of_primes = 0
    length = 0
    for j in range(i, len(primes)):
        sum_of_primes += primes[j]
        if sum_of_primes > 10**6:
            break
        length += 1
        if sum_of_primes in primes_set and length >= longest_length:
            answer = sum_of_primes
            longest_length = length
print(answer, longest_length)
print("%.6f seconds" % (time.time() - start_time))

# def is_prime(num):
#     return all(num % d != 0 for d in range(2, int(num**0.5) + 1))
#
# start_time = time.time()
#
# def get_primes(limit):
#     primes = [2]
#     sum_of_primes = 2
#     for i in range(3, limit, 2):
#         if is_prime(i):
#             primes.append(i)
#             sum_of_primes += i
#         if sum_of_primes > limit:
#             return primes
#
# def primes_sum(bnd):
#     primes = get_primes(bnd)
#     for x in range(len(primes), 0, -1):
#         y = 0
#         num = sum(primes[y:x+y])
#         while num < bnd:
#             end_prime = primes[-1]
#             while x + y > len(primes):
#                 end_prime += 2
#                 if is_prime(end_prime):
#                     primes.append(end_prime)
#             if is_prime(num):
#                 return num
#             y += 1
#             num = sum(primes[y:x+y])
# print(primes_sum(10**6))
# print("%.6f seconds" % (time.time() - start_time))
