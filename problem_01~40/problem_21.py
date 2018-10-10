# Problem_21
# Amicable numbers
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import time

def get_amicable_num(n):
    result = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result += i
            if i != n // i and n != n // i:
                result += n // i
    return result

start_time = time.time()
amicable_list = []
for num in range(1, 10001):
    check_num = get_amicable_num(num)
    if num == get_amicable_num(check_num) and num != check_num:
        amicable_list.extend([num, check_num])
amicable_list = set(amicable_list)
print(sum(amicable_list))
print("%.6f seconds" % (time.time() - start_time))
