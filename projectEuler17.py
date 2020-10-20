print("projectEuler17.py")

basic_nums = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
              "nine", "ten"]

teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
         "seventeen", "eighteen", "nineteen"]

tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]

hundred = "hundred"
and_word = "and"
thousand = "onethousand"

big_num = ""


def string_num_finder(i):
    num = ""
    if i <= 10:
        num += basic_nums[i]
    elif i <= 19:
        num += teens[i - 11]
    elif i <= 99:
        num += tens[(i // 10) - 2] + basic_nums[(i % 10)]
    elif i <= 999:
        num += basic_nums[(i // 100)] + hundred + and_word
        if i % 100 == 0:
            # subtract "and"
            # we only want to replace the first instance of "and"
            # will an empty string
            num = num.replace(and_word, '', 1)
        elif i % 100 <= 10:
            num += basic_nums[(i % 100)]
        elif (i % 100 >= 11) and (i % 100 <= 19):
            num += teens[(i % 100) - 11]
        else:
            num += tens[((i % 100) // 10) - 2] + basic_nums[(i % 10)]
    else:
        num += thousand
    return num


for j in range(1, 1001):
    big_num += string_num_finder(j)

# big_num += string_num_finder(346)

print(f"len(big_num) = {len(big_num)}")
# print(f"big_num = {big_num}")
