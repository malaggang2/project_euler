# Problem_39
# Integer right triangles
# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?
import time

def is_int(num):
    if int(num) == num:
        return True
    else:
        return False

start_time = time.time()

result = dict()
for a in range(1, 500):
    for b in range(1, 500):
        if is_int((a**2 + b**2)**0.5) and a + b + (a**2 + b**2)**0.5 <=1000:
            if a + b + (a**2 + b**2)**0.5 in result:
                result[a + b + (a**2 + b**2)**0.5] += 1
            else:
                result[a + b + (a**2 + b**2)**0.5] = 1
for p, freq in result.items():
    if max(result.values()) == freq:
        print(p)
print("%.6f seconds" % (time.time() - start_time))

# from math import sqrt
# from collections import Counter
# def is_int(num):
#     if int(num) == num:
#         return True
#     else:
#         return False
#
# p_list = [0 for _ in range(1001)]
# for a in range(1, 500):
#     for b in range(1, 500):
#         if is_int(sqrt(a**2 + b**2)) and a + b + sqrt(a**2 + b**2) <= 1000:
#             p_list[a + b + int(sqrt(a**2 + b**2))] += 1
# print(p_list.index(max(p_list)))
#
# answer_list = [a + b + int(sqrt(a**2 + b**2)) for a in range(1, 500) \
#     for b in range(1, 500) if is_int(sqrt(a**2 + b**2)) and a + b + sqrt(a**2 + b**2) <= 1000]
# print(Counter(answer_list).least_common(2))
