# Problem_60
# Prime pair sets
# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order
# the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set of four primes
# with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate
# to produce another prime.
import time

start_time = time.time()

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for d in range(3, int(num**0.5) + 1, 2):
        if num % d == 0:
            return False
    return True

def test(a, b):
    m = int(f"{a}{b}")
    n = int(f"{b}{a}")
    return is_prime(m) and is_prime(n)

def find_result(input, level=0):
    if level == 0:
        return set()
    for a in sorted(input):
        sub_primes = {x for x in input if x != a and test(x, a)}
        if len(sub_primes) < level - 1:
            continue
        result = find_result(sub_primes, level - 1)
        if result is not None:
            result.add(a)
            return result
    return None

primes = {x for x in range(3, 10**4, 2) if is_prime(x)}
result = find_result(primes, 5)
print(result, sum(result))
