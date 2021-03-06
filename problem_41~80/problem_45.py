# Problem_45
# Triangular, pentagonal, and hexagonal
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.

import time

start_time = time.time()

hexagonals = set()
pentagonals = set()
i = 1

while len(hexagonals & pentagonals) < 3:
    hexagonals.update(int(n*(2*n-1)) for n in range((i-1)*1000 + 1,i*1000 + 1))
    pentagonals.update(int(n*(3*n-1)/2) for n in range((i-1)*1000 + 1,i*1000 +1))
    i += 1
print(hexagonals & pentagonals)
print('%.6f seconds' % (time.time() - start_time))
