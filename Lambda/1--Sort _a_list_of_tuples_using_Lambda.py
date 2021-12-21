# Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

original_tuples = [
    ('English', 88),
    ('Science', 90),
    ('Maths', 97),
    ('Social sciences', 82)
]

sort_by_num = lambda x : x[1]

original_tuples.sort(key = sort_by_num)

print(original_tuples)