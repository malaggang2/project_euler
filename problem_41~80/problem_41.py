# Problem_41
# Pandigital prime
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

import time

def is_prime(n):
    if n == 1:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

def is_pandigital(n):
    for d in range(1, len(str(n))+1):
        if str(n).count(str(d)) != 1:
            return False
    return True


start_time = time.time()
for i in range(7654321, 7123456, -1):
    if is_prime(i) and is_pandigital(i):
        print(i)
        break
print("%.6f seconds" % (time.time() - start_time))

# from itertools import permutations
# t1 = time.time()
# print(max([int(''.join(i)) for i in permutations('1234567') if is_prime(int(''.join(i)))]))
# print("%.6f seconds" % (time.time() - t1))
