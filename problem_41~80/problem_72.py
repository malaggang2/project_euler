# Problem_72
# Counting fractions
# Consider the fraction, n/d, where n and d are positive integers.
# If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 21 elements in this set.
# How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

import time

start_time = time.time()

phi_list = [n for n in range(10**6+1)]
phi_list[1] = 0
prime_list = phi_list[:]
for i in range(2, len(prime_list)):
    if prime_list[i] != 0:
        p = prime_list[i]
        for j in range(i, len(prime_list), i):
            phi_list[j] *= (1-1/p)
            prime_list[j] = 0
print(int(sum(phi_list)))
print("%.6f seconds" % (time.time() - start_time))

# start_time = time.time()
#
# def get_prime_factor(num):
#     if num == 2:
#         return {2}
#     prime_factor = set()
#     d = 2
#     while True:
#         if num % d == 0:
#             num //= d
#             prime_factor.add(d)
#         else:
#             d += 1
#         if d > int(num**0.5):
#             prime_factor.add(num)
#             break
#         if num == 1:
#             prime_factor.add(d)
#             break
#     return prime_factor
#
# def get_phi(num):
#     prime_factor = get_prime_factor(num)
#     phi = num
#     for p in prime_factor:
#         phi *= (1-1/p)
#     return int(phi)
#
# result = 0
# for i in range(2, 10**6+1):
#     result += get_phi(i)
# print(result)
# print("%.6f seconds" % (time.time() - start_time))
