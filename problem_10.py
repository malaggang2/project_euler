# Problem_10
# Summation of primes
# he sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import time

def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start_time = time.time()
result = 2
for j in range(3, 2000000, 2):
    if is_prime(j):
        result += j
print(result)
print("%.6f seconds" % (time.time() - start_time))


# def euler010(number):
#     prime = [[n, False] for n in range(2,number + 1)]
#     sumOfNum = 0
#     startTime = time.time()
#     for n in range(len(prime)):
#         if (prime[n][1] == False):
#             sumOfNum += prime[n][0]
#             for nn in range(n, len(prime), prime[n][0]):
#                 prime[nn][1] = True
#     endTime = time.time()
#     print(sumOfNum)
#     print(endTime - startTime)
#
# euler010(2000000)
