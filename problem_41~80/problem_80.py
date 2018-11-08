# Problem_80
# Square root digital expansion
# It is well known that if the square root of a natural number is not an integer,
# then it is irrational. The decimal expansion of such square roots is infinite
# without any repeating pattern at all.
# The square root of two is 1.41421356237309504880..., and the digital sum of
# the first one hundred decimal digits is 475.
# For the first one hundred natural numbers, find the total of the digital sums
# of the first one hundred decimal digits for all the irrational square roots.
import time

start_time = time.time()

result = []
for n in range(2, 101):
    if int(n**0.5) != n**0.5:
        num = int(n**0.5)
        exp = 2
        while True:
            for d in range(10):
                if int(str(num)+str(d))**2 > n*10**exp:
                    d -= 1
                    break
            num = int(str(num) + str(d))
            if len(str(num)) == 100:
                break
            exp += 2
        result.append(sum(int(d) for d in str(num)))
print(sum(result))
print("%.6f seconds" % (time.time() - start_time))
