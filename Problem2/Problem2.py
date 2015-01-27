
cache = {1: 1, 2: 2}

def Fibonacci(x):
    if cache.has_key(x):
        return cache[x]

    value = Fibonacci(x-1) + Fibonacci(x-2)
    cache[x] = value
    return value

sum = 0
i = 1
max = 4000000

while True:
    value = Fibonacci(i)
    i += 1

    if value > max:
        break

    if (value % 2) == 0:
        sum += value

print sum
