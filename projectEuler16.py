print("projectEuler16.py")

num = 2 ** 1000
string = str(num)
total = 0
for i in string:
    total += int(i)

print(f"total = {total}")
