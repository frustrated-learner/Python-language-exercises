# Write a Python program to add three given lists using Python map and lambda

ls_1 = [1, 2, 3] 
ls_2 = [4, 5, 6]
ls_3 = [30, 12, 2021]

adder = lambda x, y, z : (x + y + z)

result = list(map(adder, ls_1, ls_2, ls_3))

print(result)