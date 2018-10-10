# Problem_17
# Number letter counts

numbers = {'0' : '', '1' : 'one', '2': 'two', '3':'three', '4':'four', '5':'five', '6':'six',
           '7':'seven', '8':'eight', '9':'nine', '10':'ten', '11':'eleven', '12':'twelve',
           '13':'thirteen', '14':'fourteen', '15':'fifteen','16':'sixteen', '17':'seventeen',
           '18':'eighteen', '19':'nineteen', '20':'twenty', '30':'thirty', '40':'forty',
           '50':'fifty', '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety'}

result = len('onethousand')
for hund in range(10):
    if hund == 0:
        for i in range(0, 91, 10):
            if i == 0:
                for j in range(11):
                    result += len(numbers[str(j)])
            elif i == 10:
                for j in range(11, 20):
                    result += len(numbers[str(j)])
            else:
                for j in range(10):
                    result += len(numbers[str(i)]+numbers[str(j)])
    else:
        for i in range(0, 91, 10):
            if i == 0:
                result += len(numbers[str(hund)]+"hundred")
                for j in range(1, 11):
                    result += len(numbers[str(hund)]+"hundredand"+numbers[str(j)])
            elif i == 10:
                for j in range(11, 20):
                    result += len(numbers[str(hund)]+"hundredand"+numbers[str(j)])
            else:
                for j in range(10):
                    result += len(numbers[str(hund)]+"hundredand"+numbers[str(i)]+numbers[str(j)])
print(result)

# total = 0
# for i in range(0, 10):          #100의 자리
#     if numbers[str(i)] == '':
#         hund = ''
#     else:
#         hund = numbers[str(i)] + "hundred"
#     for j in range(0, 100):     #10이하 자리
#         if j == 0:
#             ten = ''
#             print(hund+ten, "===", len(hund+ten))
#             total += len(hund+ten)
#         elif j < 21:
#             if hund == '':
#                 ten = numbers[str(j)]
#             else:
#                 ten = 'and' + numbers[str(j)]
#             print(hund+ten, "===", len(hund+ten))
#             total += len(hund+ten)
#         else:
#             if hund == '':
#                 ten = numbers[str(j)[0]+'0'] + numbers[str(j)[1]]
#             else:
#                 ten = 'and' + numbers[str(j)[0]+'0'] + numbers[str(j)[1]]
#             print(hund+ten, "===", len(hund+ten))
#             total += len(hund+ten)
# total += len("onethousand")
# print(total)
