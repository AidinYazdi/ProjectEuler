def find_triple():
    nums = [0, 0, 0]
    for a in range(1001):
        for b in range(a + 1, 1001):
            for c in range(b + 1, 1001):
                if (((a ** 2) + (b ** 2)) == (c ** 2)) and ((a + b + c) == 1000):
                    nums[0] = a
                    nums[1] = b
                    nums[2] = c
                    return nums


print(find_triple())
