# Problem_74
# Digit factorial chains
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
# it turns out that there are only three such loops that exist:
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop.
# For example,
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain
# with a starting number below one million is sixty terms.
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

import time

start_time = time.time()
factorials = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
cache = dict()
for num in range(2, 10**6+1):
    if num in cache:
        continue
    tmp = 0
    chains = [num]
    while True:
        chk_num = sum(factorials[int(i)] for i in str(num))
        if chk_num in cache:
            tmp = cache[chk_num]
            break
        if chk_num in chains:
            break
        chains.append(chk_num)
        num = chk_num
    for i in range(len(chains)):
        cache[chains[i]] = len(chains) + tmp - i
print(len([1 for k, v in cache.items() if k <= 10**6 and v == 60]))
print("%.6f seconds" % (time.time() - start_time))
