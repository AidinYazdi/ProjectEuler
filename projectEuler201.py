# setting up the initial array
s = []

s = [1, 2, 3, 4, 5, 6]

# for x in range(0, 100):
#     s.append((x + 1) ** 2)


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
def lowest(in_arr, out_arr):
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


# return an array of all the unique sums
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
    # check if the given number has either:
    # no possible combinations
    # one possible combination
    # more than one possible combination
    i = my_sum(in_arr)
    end_amount = my_sum(out_arr) + 1
    print(in_arr)
    print(out_arr)
    print(f"my_sum(in_arr) = {my_sum(in_arr)}")
    print(f"my_sum(out_arr) = {my_sum(out_arr)}")
    while i in range(end_amount):
        print(f"i = {i}")
        # while there are less than two possibilities,
        # it is still possible that the number has another sum
        possibilities = 0
        temp_in_arr = in_arr
        temp_out_arr = out_arr
        to_large_counter = len(in_arr) - 1
        to_small_counter = len(in_arr) - 1
        already_assigned = False
        make_big = False
        mixed = False
        done_checking = False
        print(f"i = {i}")
        print(f"in_arr = {in_arr}")
        print(f"out_arr = {out_arr}")
        while possibilities < 2:
            print(f"possibilities = {possibilities}")
            print(f"sums = {sums}")
            # sort the arrays so that it will be easier to swap elements out between them
            temp_in_arr.sort()
            temp_out_arr.sort()
            # the sum of the in_arr[]
            current_num = my_sum(in_arr)
            # if we've already been through all the possible combinations
            if (current_num > i) and (to_large_counter < 0):
                possibilities = 3
                done_checking = True
            elif (current_num < i) and (to_small_counter < 0):
                possibilities = 3
                done_checking = True
            # if in_arr is too large
            if ((current_num > i) or (make_big)) and (to_large_counter > 0):
                make_big = False
                temp_out_index = lowest_big(in_arr[to_large_counter], out_arr)
                if temp_out_index == -2:
                    possibilities = 3
                else:
                    temp_in_arr[to_large_counter], temp_out_arr[temp_out_index] = temp_out_arr[temp_out_index], temp_in_arr[to_large_counter]
                    to_large_counter -= 1
                    mixed = True
                    print("MADE BIGGER")
            elif (current_num < i) and (to_small_counter > 0):
                # if in_arr is too small
                temp_out_index = largest_small(in_arr[to_small_counter], out_arr)
                if temp_out_index == -2:
                    possibilities = 3
                else:
                    temp_in_arr[to_small_counter], temp_out_arr[temp_out_index] = temp_out_arr[temp_out_index], temp_in_arr[to_small_counter]
                    to_small_counter -= 1
                    mixed = True
                    print("MADE SMALLER")
            else:
                # if in_arr is unique
                if not already_assigned:
                    sums.append(i)
                    already_assigned = True
                    possibilities += 1
                    make_big = True
                else:
                    if mixed and (not done_checking):
                        print(f"done_checking = {done_checking}")
                        # duplicates.append(sums[-1])
                        del sums[-1]
                        print(f"in_arr = {in_arr}")
                        print(f"out_arr = {out_arr}")
                        print("DELETED")
                    possibilities = 3
        # sort the arrays, and then iterate "i" to the next possible value
        in_arr.sort()
        out_arr.sort()
        temp_index = lowest(in_arr, out_arr)
        # double check that the sum isn't a duplicate
        # if sums[-1] in duplicates:
        #     del sums[-1]
        # if there are still more sums
        if temp_index[0] != -2:
            print("mixed")
            in_arr[temp_index[0]], out_arr[temp_index[1]] = out_arr[temp_index[1]], in_arr[temp_index[0]]
            i = my_sum(in_arr)
            print(f"in_arr = {in_arr}")
            print(f"out_arr = {out_arr}")
        else:
            break
    # print(f"duplicates = {duplicates}")
    # return the array of all the sums
    return sums


print(f"u(s, 3) = {u(s, 3)}")
