# setting up the initial array
s = []

s = [1, 2, 3, 4, 5, 6]

# for x in range(0, 100):
#     s.append((x + 1) ** 2)


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


# the largest element in the array that is smaller than the number
def largest_small(num, arr):
    index = -2
    difference = 10001
    for i in range(len(arr)):
        if (arr[i] < num) and ((num - arr[i]) < difference):
            index = i
            difference = num - arr[i]
    return index


# the lowest element in the array that is bigger than the number
def smallest_large(num, arr):
    index = -2
    difference = 10001
    for i in range(len(arr)):
        if (arr[i] > num) and ((arr[i] - num) < difference):
            index = i
            difference = arr[i] - num
    return index


# check if the current sum has another possible solution (a duplicate)
# the arrays should be sorted before they are passed in
def check_if_duplicate(in_arr, out_arr):
    # whether or not the current sum is a duplicate
    is_a_duplicate = False
    # the sum we are trying to duplicate
    desired_sum = sum(in_arr)
    # what index of the array we are on for making in_arr larger or smaller
    # if we want to make the array larger
    to_small_counter = len(in_arr) - 1
    # if we want to make the array smaller
    to_large_counter = len(in_arr) - 1
    # how many possibilities have currently been found
    possibilities = 1
    # temporary arrays which can be modified to find new possible solutions
    temp_in_arr = in_arr.copy()
    temp_out_arr = out_arr.copy()
    # whether or not we are on the first iteration (where we will have the correct sum
    # by definition)
    first = True
    while possibilities < 2:
        # if we are on the first iteration, make in_array larger and continue
        # in_arr and out_arr are sorted for this first iteration
        if first:
            temp_index = smallest_large(temp_in_arr[to_small_counter], temp_out_arr)
            temp_in_arr[to_small_counter], temp_out_arr[temp_index] = temp_out_arr[temp_index], temp_in_arr[to_small_counter]
            to_small_counter -= 1
            first = False
        # the sum that we are currently on
        current_sum = sum(temp_in_arr)
        # if the sum a duplicate
        if desired_sum == current_sum:
            # iterate the number of possibilities
            possibilities = 2
            # mark this sum as a duplicate
            is_a_duplicate = True
            # if the sum is too large
        elif (current_sum > desired_sum) and (to_large_counter >= 0):
            # find the largest value in temp_out_arr that is smaller
            # than temp_in_arr[to_large_counter]
            temp_index = largest_small(temp_in_arr[to_large_counter], temp_out_arr)
            # iterate the to_large_counter
            to_large_counter -= 1
            # if largest_small exists (meaning, there exists at least one value
            # left in temp_out_arr that is less than temp_in_arr[to_large_counter])
            if temp_index != -2:
                temp_in_arr[to_large_counter], temp_out_arr[temp_index] = temp_out_arr[temp_index], temp_in_arr[to_large_counter]
            # if the sum is too small
        elif (current_sum < desired_sum) and (to_small_counter >= 0):
            # find that smallest value in temp_out_arr that is larger
            # than temp_in_arr[to_small_counter}
            temp_index = smallest_large(temp_in_arr[to_small_counter], temp_out_arr)
            # iterate the to_small counter
            to_small_counter -= 1
            # if smallest_large exists (meaning, there exists at least one value
            # left in temp_out_arr that is greater than temp_in_arr[to_small_counter])
            if temp_index != -2:
                temp_in_arr[to_small_counter], temp_out_arr[temp_index] = temp_out_arr[temp_index], temp_in_arr[to_small_counter]
            # if we've run out of things to switch out in the in_arr but
            # the sum is still not a duplicate
        else:
            # iterate possibilities to 2 without marking the sum as a duplicate
            possibilities = 2
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
    current_sum = sum(in_arr)
    # the maximum sum that could exist
    max_sum = sum(out_arr)
    # iterate through all the possible sums
    while current_sum <= max_sum:
        # sort the arrays before we check for a duplicate
        in_arr.sort()
        out_arr.sort()
        # NOTE: for some reason, the function duplicate() is changing the values
        # of in_arr and out_arr
        # check if the current_sum has a duplicate
        duplicate = check_if_duplicate(in_arr, out_arr)
        # if current_sum does not have a duplicate, add it to the sums[] list
        if not duplicate:
            sums.append(current_sum)
        # iterate the in_arr[] and out_arr[] and current_sum
        # index is in the form: [in_arr_index, out_arr_index]
        index = lowest_difference(in_arr, out_arr)
        if index[0] == -2:
            break
        else:
            print(f"in_arr = {in_arr}")
            print(f"out_arr = {out_arr}")
            print(f"index = {index}")
            # make in_arr larger
            in_arr[index[0]], out_arr[index[1]] = out_arr[index[1]], in_arr[index[0]]
            # iterate sum
            current_sum = sum(in_arr)
    # return the array of all the sums
    return sums


print(f"u(s, 3) = {u(s, 3)}")
