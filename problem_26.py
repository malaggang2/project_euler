# Problem_26
# Reciprocal cycles
# A unit fraction contains 1 in the numerator. The decimal representation of the
# unit fractions with denominators 2 to 10 are given:
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.
import time

start_time = time.time()

longest_reccuring_cycle = 0
answer = 0
for n in range(1, 1000, 2):
    recurring_cycle = ''
    denominators = [1]
    d = 1
    while d % n != 0:
        if d < n:
            d *= 10
        recurring_cycle += str(d // n)
        d = d % n
        if d not in denominators:
            denominators.append(d)
        else:
            recurring_cycle = recurring_cycle[denominators.index(d):]
            break
    else:
        recurring_cycle = ''
    if len(recurring_cycle) > longest_reccuring_cycle:
        longest_reccuring_cycle = len(recurring_cycle)
        answer = n
print(answer, longest_reccuring_cycle)
print("%.6f seconds" % (time.time() - start_time))
