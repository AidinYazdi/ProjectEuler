print("projectEuler12.py")
num = 0


def num_factors(x):
    factors = 0
    temp = int(x ** (1 / 2))
    while temp >= 1:
        if x % temp == 0:
            factors += 1
        temp -= 1
    factors *= 2
    return factors


counter = 1
i = 1
while i < 100000000:
    if num_factors(i) > 500:
        num = i
        break
    if counter % 100 == 0:
        print(f"counter = {counter}")
    counter += 1
    i += counter

print(f"num = {num}")
