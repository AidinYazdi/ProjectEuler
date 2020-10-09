square_first = 0
sum_first = 0
for i in range(1, 101):
    square_first += (i ** 2)
    sum_first += i
    # print(i)

sum_first = sum_first ** 2
print(sum_first - square_first)
print(f"square_first = {square_first}")
print(f"sum_first = {sum_first}")
