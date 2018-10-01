# Problem_27
# Euler discovered the remarkable quadratic formula:
# n^2+n+41
# It turns out that the formula will produce 40 primes for the consecutive
# integer values  0≤ n ≤39
# However, when n=40,402+40+41=40(40+1)+41 is divisible by 41,
# and certainly when n=41,41^2+41+41 is clearly divisible by 41.
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes
# for the consecutive values 0≤n≤79. The product of the coefficients,
# −79 and 1601, is −126479.
# Considering quadratics of the form:
# n2+an+b, where |a|<1000 and |b|≤1000
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n=0.
import time

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

start_time = time.time()
max_count = 0
for a in range(-62, 63):
    for b in range(int(a**2/4), 1000):
        prime_count = 0
        num = 0
        while True:
            chk_num = int(num**2 + num*a + b)
            if is_prime(chk_num):
                prime_count +=1
                num += 1
            else:
                break
        if prime_count > max_count:
            max_count = prime_count
            coefficients = [a, b]
            answer = a * b

print(max_count, coefficients, answer)
print("%.6f seconds" % (time.time() - start_time))
