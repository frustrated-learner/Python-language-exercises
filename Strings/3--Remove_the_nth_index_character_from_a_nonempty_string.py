# Write a Python program to remove the nth index character from a nonempty string

user_input = str(input("Enter the String : "))
removal_index = int(input("Enter the Removal position / index : "))

str_to_list = list(user_input)
final_answer = ""

del str_to_list[removal_index]

for chars in str_to_list:
    final_answer += chars

print(f"\nThe Modified string : {final_answer}")
