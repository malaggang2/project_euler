# Problem_62
# Cubic permutations
# The cube, 41063625 (345^3), can be permuted to produce two other cubes:
# 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits
# which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.
import time

start_time = time.time()

freq = dict()
for n in range(345, 10**4):
    chk = tuple(sorted(list(str(n**3))))
    if chk not in freq:
        freq[chk] = [n**3, 1]
    else:
        freq[chk][1] += 1
        if freq[chk][1] == 5:
            print(freq[chk][0])
            break
print(freq)
print(f"{time.time() - start_time} seconds")
