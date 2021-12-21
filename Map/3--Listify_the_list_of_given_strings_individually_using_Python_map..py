# Write a Python program to listify the list of given strings individually using Python map.

original_arr = ["This", "is", "Python", "Language"]

listify = lambda x : list(x)

modded_ls = list(map(listify, original_arr))

print(modded_ls)