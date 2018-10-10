# Problem_28
# Number spiral diagonals
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
# in the same way?

answer = 1
sum_num = 1
for n in range(1, 501):
    count = 1
    while count < 5:
        sum_num += 2*n
        answer += sum_num
        count += 1
print(answer)

# 수열 활용
# def sum_of_spiral(n):
#     if n == 1:
#         return 1
#     return 16*(n**2) - 28*n + 16
#
# sum = 0
# for i in range(1, 502):
#     sum += sum_of_spiral(i)
# print(sum)
