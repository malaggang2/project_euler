# Problem_31
# Coin Sums
# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
import time

start_time = time.time()
count = 0
for a in range(0, 201, 200):
    for b in range(0, 201-a, 100):
        for c in range(0, 201-a-b, 50):
            for d in range(0, 201-a-b-c, 20):
                for e in range(0, 201-a-b-c-d, 10):
                    for f in range(0, 201-a-b-c-d-e, 5):
                        for g in range(0, 201-a-b-c-d-e-f, 2):
                            for h in range(0, 201-a-b-c-d-e-f-g, 1):
                                if a+b+c+d+e+f+g+h == 200:
                                    count += 1
print(count)
print("%.6f seconds" % (time.time() - start_time))


coins = (1, 2, 5, 10, 20, 50, 100, 200)
amount = 200
answers = [1] + [0] * amount

for coin in coins:
    for i in range(coin, len(answers)):
        answers[i] = answers[i] + answers[i-coin]
print(answers[-1])
