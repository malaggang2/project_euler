# Problem_08
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import time

start_time = time.time()
for a in range(1, 333):
    for b in range(a+1, 500):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            result = a*b*c
print(result)
print("%.6f seconds" % (time.time() - start_time))
