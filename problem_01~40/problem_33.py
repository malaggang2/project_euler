# Problem_33
# Digit cancelling fractions
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than
# one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.
import time

start_time = time.time()

nums = 1
denos = 1
for a in range(10, 99):
    if a % 10 !=0:
        for b in range(a+1, 100):
            if b % 10 !=0:
                for i in range(1, 10):
                    numerator = list(str(a))
                    denominator = list(str(b))
                    if str(i) in numerator and str(i) in denominator:
                        numerator.remove(str(i))
                        denominator.remove(str(i))
                        if a / b == int(numerator[0]) / int(denominator[0]):
                            nums *= int(numerator[0])
                            denos *= int(denominator[0])

for i in range(nums, 1, -1):
    if nums % i == 0 and denos % i == 0:
        nums //= i
        denos //= i
        break
print(denos)
print("%.6f seconds" % (time.time()-start_time))
