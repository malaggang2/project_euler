# Problem_58
# Spiral primes
# Starting with 1 and spiralling anticlockwise in the following way,
# a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal,
# but what is more interesting is that 8 out of the 13 numbers lying along both diagonals
# are prime; that is, a ratio of 8/13 ≈ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral
# with side length 9 will be formed. If this process is continued,
# what is the side length of the square spiral for which the ratio of primes
# along both diagonals first falls below 10%?
import time

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for d in range(3, int(num**0.5) + 1, 2):
        if num % d == 0:
            return False
    return True

start_time = time.time()
diagonal_list = [1]
prime_list = []
n = 1
while True:
    for i in range(4):
        diagonal = diagonal_list[-1] + (2*n)
        diagonal_list.append(diagonal)
        if is_prime(diagonal):
            prime_list.append(diagonal)
    prime_ratio = (len(prime_list) / len(diagonal_list)) * 100
    if prime_ratio < 10:
        break
    n += 1
print(2*n + 1)
print("%.6f seconds" % (time.time() - start_time))

# start_time = time.time()
# diagonal = 1
# prime_count = 0
# n = 1
# while True:
#     for i in range(4):
#         diagonal += 2*n
#         if is_prime(diagonal):
#             prime_count += 1
#     prime_ratio = prime_count / (4*n + 1)
#     if prime_ratio < 0.1:
#         break
#     n += 1
# print(2*n + 1)
# print("%.6f seconds" % (time.time() - start_time))
