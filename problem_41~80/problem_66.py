# Problem_66
# Diophantine equation
# Consider quadratic Diophantine equations of the form:
# x^2 – D*y^2 = 1
# For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.
# It can be assumed that there are no solutions in positive integers when D is square.
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#
# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1
#
# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
#
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

import time

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

start_time = time.time()

answer = 0
largest_x = 0
for D in range(2, 10**3+1):
    if D**0.5 != int(D**0.5):
        found = False
        n = 1
        while not found:
            period = get_periods(D)
            x, y = get_fraction(n, period)
            if x**2 - D*(y**2) == 1:
                found = True
                if x > largest_x:
                    largest_x = x
                    answer = D
            n += 1

print(answer)
print("%.6f seconds" % (time.time() - start_time))

max_x = max_n = 0
for n in range(1001):
    r = n ** 0.5
    num, den = 1, int(r)
    if den ** 2 != n:
        x, x_prev, y, y_prev = den, 1, 1, 0
        while x ** 2 - n * y ** 2 != 1:
            this_den = (n - den ** 2) // num
            a = int((r + den) / this_den)
            x, x_prev = x * a + x_prev, x
            y, y_prev = y * a + y_prev, y
            num, den = this_den, a * this_den - den
        if x > max_x:
            max_x, max_n = x, n

print(max_n)
