# Power digit sum
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?

def power_digit_sum(num):
    return sum([int(x) for x in str(2**num)])

print(power_digit_sum(1000))
