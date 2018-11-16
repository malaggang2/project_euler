# Problem_85
# Counting rectangles
import time

start_time = time.time()

def get_num_of_rectangles(x, y):
    return int(x*y*(x+1)*(y+1)/4)

min_difference = 2000000
found = False
for i in range(2, 100):
    for j in range(1, i):
        difference = abs(2000000 - get_num_of_rectangles(i, j))
        if difference < min_difference:
            min_difference = difference
            result = i * j
print(result)
print('%.6f seconds' % (time.time() - start_time))
