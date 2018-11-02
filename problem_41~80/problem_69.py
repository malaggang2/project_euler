# Problem_69
# Totient maximum
# Euler's Totient function, φ(n) [sometimes called the phi function], is used to
# determine the number of numbers less than n which are relatively prime to n.
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively
# prime to nine, φ(9)=6.
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
import time
from itertools import count

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for d in range(3, int(num**0.5)+1, 2):
        if num % d == 0:
            return False
    return True

start_time = time.time()

result = 1
for i in count(2):
    if is_prime(i):
        result *= i
    if result > 10**6:
        result /= i
        break
print(int(result))

print("%.6f seconds" % (time.time() - start_time))
