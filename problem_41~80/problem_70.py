# Problem_70
# Totient permutation
# Euler's Totient function, φ(n) [sometimes called the phi function],
# is used to determine the number of positive numbers less than or equal to n
# which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all
# less than nine and relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
# Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n
# and the ratio n/φ(n) produces a minimum.

import time

start_time = time.time()

nums = [n for n in range(10**6*5)]
nums[1] = 0
for i in range(2, int(len(nums)**0.5) + 1):
    if nums[i] != 0:
        for j in range(i*2, len(nums), i):
            nums[j] = 0
primes = [n for n in nums if n != 0]

min_ratio = 2
answer = None
for p in range(len(primes)):
    if primes[p] > (10**7)**0.5:
        break
    for q in range(p+1, len(primes)):
        chk_num = primes[p] * primes[q]
        if chk_num > 10**7:
            break
        if sorted(str(chk_num)) == sorted(str((primes[p] - 1)*(primes[q] - 1))):
            ratio = chk_num / ((primes[p] - 1)*(primes[q] - 1))
            if ratio < min_ratio:
                min_ratio = ratio
                answer = chk_num, primes[p], primes[q]
print(answer)
print("%.6f seconds" % (time.time() - start_time))

# start_time = time.time()
#
# def is_prime(num):
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for d in range(2, int(num**0.5) + 1):
#         if num % d == 0:
#             return False
#     return True
#
# answer = (0, 10**7)
# p = 1999
# while True:
#     if not is_prime(p):
#         p += 2
#         continue
#     q = p + 2
#     if p * q > 10**7:
#         break
#     while True:
#         if not is_prime(q):
#             q += 2
#             continue
#         chk_num = p * q
#         if chk_num > 10**7:
#             break
#         pi = (p - 1)*(q - 1)
#         if sorted(str(chk_num)) == sorted(str(pi)):
#             answer = min(answer, (chk_num, chk_num / pi), key=lambda x:x[1])
#         q += 2
#     p += 2
# print(answer[0])
# print("%.6f seconds" % (time.time() - start_time))
