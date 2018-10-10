# Problem_32
# Pandigital products
# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
#  1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to
# only include it once in your sum.
import time

start_time = time.time()
pandigitals = set()
for i in range(1, 100):
    for j in range(1000//i, 10000//i):
        product = i * j
        chk_list = sorted([int(s) for s in (str(i) + str(j) + str(product))])
        if chk_list == [n for n in range(1, 10)]:
            pandigitals.add(product)
print(sum(pandigitals))
print('%.6f seconds' % (time.time() - start_time))
