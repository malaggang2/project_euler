# Problem_64
# Odd period square roots
# All square roots are periodic when written as continued fractions and can be written in the form:
# It can be seen that the sequence is repeating. For conciseness, we use the notation
# √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.
# The first ten continued fraction representations of (irrational) square roots are:
#
# √2=[1;(2)], period=1
# √3=[1;(1,2)], period=2
# √5=[2;(4)], period=1
# √6=[2;(2,4)], period=2
# √7=[2;(1,1,1,4)], period=4
# √8=[2;(1,4)], period=2
# √10=[3;(6)], period=1
# √11=[3;(3,6)], period=2
# √12= [3;(2,6)], period=2
# √13=[3;(1,1,1,1,6)], period=5
#
# Exactly four continued fractions, for N ≤ 13, have an odd period.
#
# How many continued fractions for N ≤ 10000 have an odd period?
import time

start_time = time.time()
n = 2
answer = 0
while n <= 10**4:
    period = []
    square_n = n**0.5
    chk_fraction = [1, int(square_n)]
    fraction = [1, int(square_n)]
    while True:
        numerator = fraction[0]
        denominator = n - (fraction[1]**2)
        if numerator != 1 and denominator % numerator == 0:
            denominator //= numerator
            numerator = 1
        tmp = int((numerator*(square_n + fraction[1])) / denominator)
        period.append(tmp)
        fraction = [denominator, tmp*denominator - fraction[1]]
        if fraction == chk_fraction:
            break
    if len(period) % 2 != 0:
        answer += 1
    n += 1
    if n**0.5 == int(n**0.5):
        n += 1
print(answer)
print("%.6f seconds" % (time.time() - start_time))
