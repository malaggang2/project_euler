# problem solving
sum = 0
for i in range(1, 1000):
    if (i % 3 == 0) or (i % 5 == 0):
        sum += i
print(sum)

# making reusable function
# input number 이하의 수 중에서 두 수의 배수의 합을 구하는 함수
def sumOfMultiples(num, multiple_by_first, multiple_by_second):
    sum = 0
    for i in range(1, num):
        if (i % multiple_by_first == 0) or (i % multiple_by_second == 0):
            sum += i
    return sum

print(sumOfMultiples(1000, 3, 5))
