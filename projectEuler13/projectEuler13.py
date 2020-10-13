nums = []

f = open("projectEuler13.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    nums.append(int(line))
f.close()

my_sum = sum(nums)

print(str(my_sum)[0:10])
