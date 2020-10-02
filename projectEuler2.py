# 1, 2, 3, 5

n1 = 1
n2 = 2
current = 0
total = 2
numTerm = 1

while numTerm <= 2000:
    current = n1 + n2
    n1 = n2
    n2 = current
    if (current % 2) == 0:
        total += current
    numTerm += 1

# print(total)
print(current)
