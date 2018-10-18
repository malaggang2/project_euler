# Problem_51
# Prime digit replacements
# By replacing the 1st digit of the 2-digit number *3,
# it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit,
# this 5-digit number is the first example having seven primes among the ten generated numbers,
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number
# (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
import time
from itertools import product, permutations, count

def is_prime(num):
    return all(num % d != 0 for d in range(2, int(num**0.5) + 1))

def prime_generator():
    yield 2
    for n in count(3, 2):
        if is_prime(n):
            yield n

start_time = time.time()
for n in prime_generator():
    for repeat_num in '01':
        property_count = 0
        no_count = 0
        properties = []
        if str(n).count(repeat_num) >= 2:
            for k in '0123456789':
                new_num = str(n).replace(repeat_num, k)
                if is_prime(int(new_num)) and int(new_num) >= n:
                    property_count += 1
                    properties.append(new_num)
                else:
                    no_count += 1
                if no_count > 2:
                    break
        if property_count == 8:
            print(properties)
            print('%.6f seconds' % (time.time() - start_time))
            exit()
