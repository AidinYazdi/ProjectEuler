largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        str_num = str(num)
        is_palindrome = True
        for l in range(len(str_num) // 2):
            if str_num[l] != str_num[(len(str_num) - 1) - l]:
                is_palindrome = False
        if is_palindrome:
            if largest < num:
                largest = num
        # print(f"num = {num}")
        # print(f"is_palindrome = {is_palindrome}")

print(largest)
