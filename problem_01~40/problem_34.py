# Problem_34
# Digit factorials
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
import time

start_time = time.time()
factorials = [1]
for i in range(1, 10):
    factorials.append(factorials[-1]*i)
limit = factorials[-1]*7
results = [n for n in range(10, limit) if n == sum(factorials[int(i)] for i in str(n))]
print(sum(results))
print('%.6f seconds' % (time.time() - start_time))
