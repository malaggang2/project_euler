# Problem_23
# Non-abundant sums
# A perfect number is a number for which the sum of its proper divisors is exactly
# equal to the number. For example, the sum of the proper divisors of 28 would
# be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.
import time

def is_abundant_num(n):
    sum_of_divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if n != n // i and i != n // i:
                sum_of_divisors += n // i
    return sum_of_divisors > n

start_time = time.time()

source = set(i for i in range(1, 28124))
abundant_list = [num for num in range(1, 28124) if is_abundant_num(num)]
new_list = set()
for n1 in abundant_list:
    for n2 in abundant_list:
        if n1 + n2 < 28124:
            new_list.add(n1+n2)
print(sum(source - new_list))
print("%.6f seconds" % (time.time() - start_time))
