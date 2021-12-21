# Write a Python program to triple all numbers of a given list of integers. Use Python map

original_num_ls = [1, 2, 3, 4, 5, 6, 7, 8]

tripler = lambda x : x * 3

modified_num_ls = list(map(tripler, original_num_ls))

print("Original List : ", original_num_ls)
print("Modified List : ", modified_num_ls)