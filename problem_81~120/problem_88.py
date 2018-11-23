# Problem_88
# Product-sum numbers
import time

start_time = time.time()

def get_products(num, divisor):
    result = []
    for d in range(divisor, int(num**0.5) + 1):
        if num % d == 0:
            result += [[d] + a for a in get_products(num//d, d)]
    result.append([num])
    return result

k_minimals = {}
for p in range(2, 24001):
    for i in get_products(p, 2):
        k = (p - sum(i)) + len(i)
        if k == 1 or k > 12000:
            continue
        if k not in k_minimals:
            k_minimals[k] = p

print(sum(set(minimal for k, minimal in k_minimals.items())))
print('%.6f seconds' % (time.time() - start_time))
