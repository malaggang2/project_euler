# Problem_43
# Sub-string divisibility
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
# In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
import time
from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]

start_time = time.time()
pandigitals = [''.join(n) for n in permutations('0123456789') if n[0] != '0' and int(n[3]) % 2 == 0 and int(n[5]) % 5 == 0 and n[-1] != '0']

answer = 0
for pandigital in pandigitals:
    for i in range(1, 8):
        if int(pandigital[i:i+3]) % primes[i-1] != 0:
            break
    else:
        answer += int(pandigital)

print(answer)
print("%.6f seconds" % (time.time() - start_time))

# def func(used, n):
#     sum = 0
#     if n == 0:
#         for a in permutations('0123456789', 4):
#             if a[0] == '0':
#                 continue
#             else:
#                 value = int(''.join(a))
#                 if value % 2 == 0:
#                     sum += func(used + list(a), n + 1)
#     else:
#         for i in filter(lambda x:x not in used, '0123456789'):
#             value = int(''.join(used[-2:] + list(i)))
#             if value % primes[n] == 0:
#                 if n == 6:
#                     value = int(''.join(used + list(i)))
#                     sum += value
#                 else:
#                     sum += func(used + list(i), n + 1)
#     return sum
#
# start_time = time.time()
# print(func([], 0))
# print('%.6f seconds' % (time.time() - start_time))
