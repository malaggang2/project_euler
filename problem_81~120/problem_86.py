# Problem_86
# cubiod route
import time
from math import gcd, sqrt

start_time = time.time()

max_M = 2000
limit = int(sqrt((2*max_M)**2 + max_M))
primitives = []
for m in range(2, int(sqrt(limit))+ 1):
    for n in range(1, m):
        if (m - n) % 2 != 0 and gcd(m, n) == 1:
            primitives.append([m**2 - n**2, 2*m*n])

triplets = []
for i in primitives:
    k = 1
    while True:
        a, b = sorted([k*i[0], k*i[1]])
        if max(a, b) > 2*max_M or min(a, b) > max_M:
            break
        if b <= 2*a:
            triplets.append([a, b])
        triplets.append([b, a])
        k += 1

triplets.sort(key=lambda x: x[0])
count = 0
c = 0
while count < 10**6:
    a, b = triplets[c]
    if a > b:
        count += b // 2
    else:
        count += int(b/2) - b + a + 1
    c += 1

print(triplets[c-1][0], count)
print('%.6f seconds' % (time.time() - start_time))
