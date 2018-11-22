# Problem_87
# Prime Power triples
# The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
# In fact, there are exactly four numbers below fifty that can be expressed in such a way:
# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4
# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
import time

start_time = time.time()
limit = 50*10**6
nums = [n for n in range(int(limit**0.5))]
nums[1] = 0
for i in range(2, int(len(nums)**0.5) + 1):
    if nums[i] != 0:
        for j in range(2*i, len(nums), i):
            nums[j] = 0

primes1 = [n**4 for n in nums if n != 0 and n <= limit**0.25]
primes2 = [n**3 for n in nums if n != 0 and n <= limit**(1/3)]
primes3 = [n**2 for n in nums if n != 0]

results = set()
for i in primes1:
    for j in primes2:
        for k in primes3:
            num = i + j + k
            if num < limit:
                results.add(num)
print(len(results))
print('%.6f seconds' % (time.time() - start_time))
