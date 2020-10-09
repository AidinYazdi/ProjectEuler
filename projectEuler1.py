total = 0
for i in range(1, 1001):
    temp = i
    if temp % 3 == 0:
        total += i
    elif temp % 5 == 0:
        total += i

print(total)
