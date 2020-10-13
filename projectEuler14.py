def series_size(num):
    size = 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = (3 * num) + 1
        size += 1
    if num == 1:
        size += 1
    return size


largest_size = 0
best_num = 0
for i in range(1, 1000000):
    temp = series_size(i)
    if temp > largest_size:
        largest_size = temp
        best_num = i
    if i % 10000 == 0:
        print(f"i = {i}")

print(f"largest_size = {largest_size}")
print(f"best_num = {best_num}")
