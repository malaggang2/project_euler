# Problem_46
# Goldbach's other conjecture
# It was proposed by Christian Goldbach that every odd composite number can
# be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime
# and twice a square?
import time

def is_prime(n):
    if n == 1:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

primes = [2] + [n for n in range(1, 10000, 2) if is_prime(n)]

def is_goldbach_correct(n):
    tmp_primes = filter(lambda x: x < n, primes)
    for prime in tmp_primes:
        tmp = ((n - prime) / 2)**0.5
        if int(tmp) == tmp:
            return True

start_time = time.time()
num_list = set(n for n in range(3, 10000, 2)) - set(primes)
for num in num_list:
    if not is_goldbach_correct(num):
        print(num)
        break
print("%.6f seconds" % (time.time() - start_time))
