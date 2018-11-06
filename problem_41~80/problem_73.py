# Problem_73
# Counting fractions in a range
# Consider the fraction, n/d, where n and d are positive integers.
# If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 3 fractions between 1/3 and 1/2.
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

import time
from math import ceil

# 첫 번째 접근
start_time = time.time()

prime_list = [n for n in range(12001)]
prime_list[1] = 0
prime_factor = [[] for n in range(12001)]
for i in range(2, len(prime_list)):
    if prime_list[i]:
        p = prime_list[i]
        for j in range(i, len(prime_list), i):
            prime_factor[j].append(p)
            prime_list[j] = 0

result = 0
for i in range(2, len(prime_factor)):
    tmp = [n for n in range(i)]
    for j in prime_factor[i]:
        for k in range(j, len(tmp), j):
            tmp[k] = 0
    result += len([n for n in tmp if n != 0 and 1/3 < (n / len(tmp)) < 1/2])
print(result)
print("%.6f seconds" % (time.time() - start_time))

# 두 번째 접근
def get_fractions(num):
    count = 0
    a, b, c, d = 0, 1, 1, num
    while c < num:
        k = int((num + b) / d)
        a, b, c, d = c, d, (c*k - a), (d*k - b)
        if 1/3 < a/b < 1/2:
            count += 1
    return count
start_time = time.time()
print(get_fractions(12000))
print("%.6f seconds" % (time.time() - start_time))

# 세 번째 접근
def counting_fractions(n):
    sieve = [0] * (n + 1)
    for i in range(5, n + 1):
        s_floor = int(i/3) + 1
        s_ceil = ceil(i/2) - 1
        s = s_ceil - s_floor + 1
        sieve[i] += s
        for j in range(2 * i, n + 1, i):
            sieve[j] -= sieve[i]
    return sum(sieve)
start_time = time.time()
print(counting_fractions(12000))
print("%.6f seconds" % (time.time() - start_time))

# prime_factor를 에라토스테네스의 체를 활용하여 구한 뒤, problem_72에 적용
# start_time = time.time()
#
# prime_list = [n for n in range(10**6+1)]
# prime_list[1] = 0
# prime_factor_list = [[] for n in range(10**6+1)]
# for i in range(2, len(prime_list)):
#     if prime_list[i]:
#         p = prime_list[i]
#         for j in range(i, len(prime_list), i):
#             prime_factor_list[j].append(p)
#             prime_list[j] = 0
#
# def get_phi(num):
#     prime_factor = prime_factor_list[num]
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
