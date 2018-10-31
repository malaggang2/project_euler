# Problem_63
# Powerful digit counts
# The 5-digit number, 16807=7^5, is also a fifth power.
# Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?
import time

start_time = time.time()

result = 0
for i in range(1, 10):
    n = 1
    while n <= len(str(i**n)):
        if n == len(str(i**n)):
            result += 1
        n += 1
print(result)
print("%.6f seconds" % (time.time()-start_time))
