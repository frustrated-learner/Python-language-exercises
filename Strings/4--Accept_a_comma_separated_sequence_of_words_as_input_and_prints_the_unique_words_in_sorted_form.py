# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form

user_input = str(input("Enter the Words : "))
str_to_list = user_input.split(",")
final_word = ""

for index, words in enumerate(str_to_list):
    temp_words = ""
    temp_ls = list(words)
    
    for chars in temp_ls:
        if (temp_ls[0] == " "):
            del temp_ls[0]
            
    for chars_2 in temp_ls:
        temp_words += chars_2
        
    str_to_list[index] = temp_words

str_to_list = list(set(str_to_list))
str_to_list.sort()

for index, words in enumerate(str_to_list):
    if (index == len(str_to_list) - 1):
        final_word += f"{words}"
        break

    final_word += f"{words}, "

print(final_word)