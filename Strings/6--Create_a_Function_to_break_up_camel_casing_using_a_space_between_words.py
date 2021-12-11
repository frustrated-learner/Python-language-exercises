# Complete the solution so that the function will break up camel casing, using a space between words.

# Example :
# "camelCasing"    =>  "camel Casing"
# "identifier"     =>  "identifier"
# ""               =>  ""
# "helloWorld"     =>  "hello World"
# "breakCamelCase" =>  "break Camel Case"

def solution(s):
    final_string = ""
    str_to_ls = list(s)
    str_to_ls_copy = list(s)
    actual_index = 0;

    for index, chars in enumerate(str_to_ls):
        if chars.isupper() == True:
            str_to_ls_copy.insert(index + actual_index, " ")
            actual_index += 1

    for chars in str_to_ls_copy:
        final_string += chars

    return final_string


user_input = str(input("Enter the Camel Case String : "))
print(f"The Broken String => {solution(user_input)}")