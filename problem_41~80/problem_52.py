# Problem_52
# Permuted Multiples
# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.
import time
from collections import Counter

start_time = time.time()

n = 1
found = False
while not found:
    for i in range(10**n, int('1'+'6'*n) + 1):
        chk = Counter(str(i))
        for j in range(2, 7):
            new_num = str(i*j)
            if chk != Counter(new_num):
                break
        else:
            found = True
            answer = i
    n += 1
print(answer)
print("%.6f seconds" % (time.time() - start_time))
