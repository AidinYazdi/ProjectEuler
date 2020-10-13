arr = []

f = open("projectEuler11.txt", "r")
while True:
    line = f.readline()
    # if there are no more lines left
    if not line:
        break
    # split the line up based on the spaces
    int_line = line.split(' ')
    arr.append([])
    for i in int_line:
        arr[-1].append(int(i))
f.close()

largest_product = 0

for r in range(len(arr)):
    for c in range(len(arr[r])):
        # horizontal product (to the right)
        if c < (len(arr[r]) - 3):
            temp_product = arr[r][c] * arr[r][c + 1] * arr[r][c + 2] * arr[r][c + 3]
            if temp_product > largest_product:
                largest_product = temp_product
        # right-down product
        if (c < (len(arr[r]) - 3)) and (r < (len(arr) - 3)):
            temp_product = arr[r][c] * arr[r + 1][c + 1] * arr[r + 2][c + 2] * arr[r + 3][c + 3]
            if temp_product > largest_product:
                largest_product = temp_product
        # down product
        if r < (len(arr) - 3):
            temp_product = arr[r][c] * arr[r + 1][c] * arr[r + 2][c] * arr[r + 3][c]
            if temp_product > largest_product:
                largest_product = temp_product
        # left-down product
        if (c > 2) and (r < (len(arr) - 3)):
            temp_product = arr[r][c] * arr[r + 1][c - 1] * arr[r + 2][c - 2] * arr[r + 3][c - 3]
            if temp_product > largest_product:
                largest_product = temp_product

print(f"largest_product = {largest_product}")
