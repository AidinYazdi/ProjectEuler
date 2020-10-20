print("projectEuler15.py")
# IMPORTANT: The below code is too slow to do 20 rows and 20 columns.
# Instead, this problem can be solved mathematically.
# This problem is essentially 40 choose 20:
# 40C20 = (40)!/((20)!(20)!) = 137846528820 ("!" is factorial)
#
#
# def possibilities(r, c, og_r, og_c):
#     if (r == 0) and (c == 0):
#         return 1
#     elif r == 0:
#         return possibilities(r, c - 1, og_r, og_c)
#     elif c == 0:
#         return possibilities(r - 1, c, og_r, og_c)
#     else:
#         return possibilities(r - 1, c, og_r, og_c) + possibilities(r, c - 1, og_r, og_c)
#
#
# rows = 5
# columns = 5
# print(possibilities(rows, columns, rows, columns))
