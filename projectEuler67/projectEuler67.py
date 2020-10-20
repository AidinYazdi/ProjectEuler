print("projectEuler67.py")

# a 2D array with the numbers in the pyramid
pyramid = []

f = open("projectEuler67.txt", "r")
while True:
    line = f.readline()
    # if there are no more lines left
    if not line:
        break
    # split the line up based on the spaces
    int_line = line.split(' ')
    pyramid.append([])
    for i in int_line:
        pyramid[-1].append(int(i))
f.close()

for i in range(len(pyramid) - 2, -1, -1):
    for j in range(0, len(pyramid[i])):
        if pyramid[i + 1][j] > pyramid[i + 1][j + 1]:
            pyramid[i][j] += pyramid[i + 1][j]
        else:
            pyramid[i][j] += pyramid[i + 1][j + 1]

largest_path = pyramid[0][0]
print(f"largest_path = {largest_path}")
