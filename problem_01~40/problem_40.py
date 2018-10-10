# Problem_40
# Champernowne's constant
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
import time

start_time = time.time()
decimal_fraction = ''
i = 1
while len(decimal_fraction) <= 10**6:
    decimal_fraction += str(i)
    i += 1

result = 1
for j in range(7):
    result *= int(decimal_fraction[10**j - 1])
print(result)
print("%.6f seconds" % (time.time() - start_time))

# from functools import reduce
# print(reduce(lambda x, y: x * y, [int(decimal_fraction[10**i - 1]) for i in range(7)]))
