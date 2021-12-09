# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself

user_input = input(str("Enter the String : "))
the_list = list(user_input)
first_char = the_list[0]

final_output = "";

for index, chars in enumerate(the_list):
    if index != 0 and chars == first_char:
        the_list[index] = "$"

for chars in the_list:
    final_output += chars

print(f"The output : {final_output}")