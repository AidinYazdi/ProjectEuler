# setting up the initial array
s = []

# s = [1, 2, 3, 4, 5, 6]

for x in range(0, 100):
    s.append((x + 1) ** 2)


# sum up an array
def my_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total


# lowest index in out_arr that is larger than something in in_arr
# the arrays MUST be sorted before they are passed in
# returns -2 if such a value does not exist
# returns -3 if a duplicate has been found (NOT CURRENTLY IMPLEMENTED)
def lowest_difference(in_arr, out_arr):
    # index is in the format: [in_arr_index, out_arr_index]
    index = [-2, -2]
    difference = 10000
    for i in range(len(in_arr)):
        for j in range(len(out_arr)):
            temp = out_arr[j] - in_arr[i]
            if (temp > 0) and (temp <= difference):
                difference = temp
                index = [i, j]
    return index


# the lowest element in the array that is bigger than the number
def lowest_big(num, arr):
    index = -2
    for i in range(len(arr)):
        if arr[i] > num:
            index = i
            return index
    return index


# the largest element in the array that is smaller than the number
def largest_small(num, arr):
    index = -2
    for i in range(len(arr)):
        if arr[i] < num:
            index = i
    return index


# check if the current sum has another possible solution (a duplicate)
def check_if_duplicate(in_arr, out_arr):
    is_a_duplicate = False
    return is_a_duplicate


# return an array of all the unique sums
# this code will work ONLY if we are choosing half the numbers in the total array
# for instance: finding sub arrays of 3 from an array of 6 will work, but finding
# sub arrays of 2 from an array of 6 will not work
def u(arr, num):
    # the array which will keep track of all the unique sums
    sums = []
    # duplicates = []
    # divide the array into one array which will be used to check if the sum
    # exists and another array of the numbers which are not being used
    in_arr = []
    out_arr = []
    for i in range(num):
        in_arr.append(arr[i])
    for i in range(num, len(arr)):
        out_arr.append(arr[i])
    # iterate through the smallest possible sum to the largest possible sum
    # add the given number (the given sum) to the sums[] list
    # check if the given number has another list of addends (since each number we iterate
    # to must have at least one solution by definition)
    # if the given number has another possible list of addends, remove it from the sums[] list
    # the sum we are on:
    current_sum = my_sum(in_arr)
    # the maximum sum that could exist
    max_sum = my_sum(out_arr)
    # iterate through all the possible sums
    while current_sum <= max_sum:
        print(f"current_sum = {current_sum}")
        # check if the current_sum has a duplicate
        duplicate = check_if_duplicate(in_arr, out_arr)
        # if current_sum does not have a duplicate, add it to the sums[] list
        if not duplicate:
            sums.append(current_sum)
        # iterate the in_arr[] and out_arr[] and current_sum
        index = lowest_difference(in_arr, out_arr)
        if index[0] == -2:
            break
        else:
            # make in_arr larger
            in_arr[index[0]], out_arr[index[1]] = out_arr[index[1]], in_arr[index[0]]
            # iterate sum
            current_sum = my_sum(in_arr)
    # return the array of all the sums
    print(f"len(sums) = {len(sums)}")
    return sums


print(f"u(s, 3) = {u(s, 50)}")
