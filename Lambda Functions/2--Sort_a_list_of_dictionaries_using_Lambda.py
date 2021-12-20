# Write a Python program to sort a list of dictionaries using Lambda. Go to the editor

# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

original_list = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

sort_by_make = lambda x : x["make"]
sort_by_model = lambda x : int(x["model"])
sort_by_color = lambda x : x["color"]

original_list.sort(key = sort_by_make)
print("By Make : ")
print(original_list, end="\n\n")

original_list.sort(key = sort_by_model)
print("By Model : ")
print(original_list, end="\n\n")

print("By Color : ")
original_list.sort(key = sort_by_color)
print(original_list, end="\n\n")