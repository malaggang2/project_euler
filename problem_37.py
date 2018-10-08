# Problem_37
# Truncatable primes
# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right
# and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import time
from itertools import product

def is_prime(n):
    if n == 1:
        return False
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True

start_time = time.time()
result = []
i = 1
while len(result) != 11:
    for head in product('2357', repeat=1):
        for body in product('1379', repeat=i):
            chk_num = ''.join(head) + ''.join(body)
            if is_prime(int(chk_num)) and not chk_num.endswith('1') and not chk_num.endswith('9'):
                tmp = []
                tmp.extend([chk_num[s:] for s in range(1, len(chk_num))])
                tmp.extend([chk_num[:t+1] for t in range(len(chk_num)-1)])
                for tmp_num in tmp:
                    if not is_prime(int(tmp_num)):
                        break
                else:
                    result.append(int(chk_num))
    i += 1
print(sum(result))
print('%.6f seconds' % (time.time() - start_time))
