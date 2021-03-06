# Problem_44
# Pentagon numbers
# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
# The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
# However, their difference, 70 − 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers,
# Pj and Pk, for which their sum and difference are pentagonal
# and D = |Pk − Pj| is minimised; what is the value of D?

import time

# start_time = time.time()
# pentagonals = list(int(n*(3*n-1)/2) for n in range(1, 3000))
# for j in range(len(pentagonals)):
#     for k in range(j + 1, len(pentagonals)):
#         if (pentagonals[j] + pentagonals[k]) in pentagonals[k:] and (pentagonals[k] - pentagonals[j]) in pentagonals[:k]:
#             print(pentagonals[k] - pentagonals[j])
# print('%.6f seconds' % (time.time() - start_time))

start_time = time.time()
pentagonals = set(int(n*(3*n-1)/2) for n in range(1, 3000))
for j in pentagonals:
    for k in pentagonals:
        if (j + k) in pentagonals and (k - j) in pentagonals:
            print(k - j)
print('%.6f seconds' % (time.time() - start_time))
