# Problem_94
# Almost equilateral triangles

# import time
# from math import gcd
#
# start_time = time.time()
#
# limit = 10**9
# answer = 0
# for m in range(2, int((limit/2)**0.5) + 1):
#     for n in range(1, m):
#         if (m - n) % 2 != 0:
#             if gcd(m, n) == 1:
#                 triangle = sorted([m**2 - n**2, 2*m*n, m**2+n**2])
#                 if abs(triangle[2] - 2*triangle[0]) == 1:
#                     perimeter = triangle[2]*2 + triangle[0]*2
#                     if perimeter < limit:
#                         answer += perimeter
# print(answer)
# print('%.6f seconds' % (time.time() - start_time))

import time

start_time = time.time()

def get_periods(num):
    """num의 제곱근의 값을 연분수 형태로 나타낼 때, 각 단계별 정수부를 구하는 함수
    반복이 되는 주기를 발견하면 연산을 멈추고, 반복되는 정수부를 리스트로 반환"""
    period = []
    square_n = num**0.5
    chk_fraction = [1, int(square_n)]
    fraction = [1, int(square_n)]
    while True:
        numerator = fraction[0]
        denominator = num - (fraction[1]**2)
        if numerator != 1 and denominator % numerator == 0:
            denominator //= numerator
            numerator = 1
        tmp = int((numerator*(square_n + fraction[1])) / denominator)
        period.append(tmp)
        fraction = [denominator, tmp*denominator - fraction[1]]
        if fraction == chk_fraction:
            break
    period.insert(0, int(num**0.5))
    # 제일 처음 시작되는 정수부가 빠져있으므로 추가
    return period

def get_fraction(nth, terms):
    """주어진 연분수의 정수부 리스트를 참고하여, n번째까지 진행한 연분수를 확장한 값의
    분자와 분모를 반환"""
    start = terms.pop(0)
    # 반복이 되지 않는 첫번째 정수부는 참고 값으로 따로 저장하며 리스트에서 삭제
    if nth == 1:
        return start, 1
    numerator, denominator = 1, terms[(nth-2) % len(terms)]
    while nth >= 3:
        pre_term = terms[(nth-3) % len(terms)]
        numerator, denominator = denominator, pre_term*denominator + numerator
        nth -= 1
    numerator, denominator = denominator, start*denominator + numerator
    # 연분수를 확장할 때, 최초의 정수값까지 확장하지는 않으므로, 위에서 저장해 둔
    # 첫번째 정수값을 한 번 더 처리함.
    return denominator, numerator

limit = 10**9
results = []
x = 2
while True:
    m, n = get_fraction(x, get_periods(3))
    if m**2 - 3*n**2 == 1:
        perimeter1 = 4*m**2
        if perimeter1 >= limit:
            break
        results.append((perimeter1))
    x += 1

x = 2
while True:
    i, n = get_fraction(x, get_periods(3))
    if i**2 - 3*n**2 == 1:
        m = i + 2*n
        perimeter2 = 2*(m+n)**2
        if perimeter2 >= limit:
            break
        results.append(perimeter2)
    x += 1
print(sum(results))
print('%.6f seconds' % (time.time() - start_time))
