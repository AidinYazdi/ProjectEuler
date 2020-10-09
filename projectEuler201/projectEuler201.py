# THIS PROBLEM IS INCOMPLETE:
# setting up the initial array
s = []

for i in range(0, 100):
    s.append((i + 1) ** 2)

# print(s)
# print(len(s))

sums = []
combinations = []
combinations_counter = 0
original_num = 50
# test_array = [1, 2, 3, 4, 5, 6]


# return an array of all the possible sums
def U(arr, num, so_far):
    if num == 0:
        global combinations
        global combinations_counter
        combinations.append([])
        for yeet in so_far:
            combinations[combinations_counter].append(yeet)
        combinations_counter += 1
        sums.append(sum(so_far))
    else:
        for i in range(len(arr)):
            if bool(so_far) and (arr[i] == so_far[-1]):
                assign = False
            else:
                assign = True
            if assign:
                so_far.append(arr[i])
                U(arr[i + 1:len(arr)], num - 1, so_far)
                del so_far[-1]


# sum up an array
def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total


# delete all the duplicate sums and add up the remaining ones
def final_function(arr):
    arr.sort()
    temp = 0
    final_total_sum = 0
    for d in range(len(arr)):
        assign = False
        if (arr[d] != temp):
            assign = True
        if ((d + 1) < len(arr)) and (arr[d + 1] == arr[d]):
            assign = False
            temp = arr[d]
        if assign == True:
            temp = arr[d]
            final_total_sum += arr[d]
    return final_total_sum


# a function to delete pairs with unique sums before writing to the file
def delete_uniques_for_writing(two_dim_arr):
    temp_sums = [0]
    for i in range(len(two_dim_arr)):
        for j in range(len(two_dim_arr[i])):
            temp_sums[i] += two_dim_arr[i][j]
        if i < len(two_dim_arr) - 1:
            temp_sums.append(0)
    # DELETE UNIQUES HERE
    return two_dim_arr


# a function to write the pairs with duplicate sums to a file
def write(two_dim_arr, file_name):
    # delete all the unique pairs
    delete_uniques_for_writing(two_dim_arr)
    f = open(file_name, "w")
    for i in range(len(two_dim_arr)):
        for j in range(len(two_dim_arr[i])):
            f.write(str(two_dim_arr[i][j]))
            if j < len(two_dim_arr[i]) - 1:
                f.write(",")
        f.write("\n")
    f.close()


file_name = "projectEuler201/pairs.txt"
# U(s, 2, [])
# print(final_function(sums))
# U(s, 2, [])
# final_function(sums)
# write(combinations, file_name)
# print(sum(s))
