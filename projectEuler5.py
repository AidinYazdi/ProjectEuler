def is_divisible(x):
    divisible = True
    for i in range(1, 21):
        if x % i != 0:
            divisible = False
    return divisible


found = False
num = 20
while not found:
    if is_divisible(num):
        print(f"actual num = {num}")
        found = True
    else:
        num += 20
    if num % 100000 == 0:
        print(f"checking num = {num}")
