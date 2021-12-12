# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this problem.

# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

# For example, decode("h3 th2r2") would return "hi there".

# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

def encode(st):
    vowels = ["a", "e", "i", "o", "u"]
    str_to_list = list(st)
    encoded_str = ""

    for index1, chars in enumerate(str_to_list):
        for index2, each_vowel in enumerate(vowels):
            if chars == each_vowel:
                str_to_list[index1] = str(index2 + 1)

    for encoded_chars in str_to_list:
        encoded_str += encoded_chars

    return encoded_str

def decode(st):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_index = [1, 2, 3, 4, 5]
    str_to_list = list(st)
    decoded_str = ""

    for index1, chars in enumerate(str_to_list):
        for index2, each_index in enumerate(vowel_index):
            if chars == str(each_index):
                str_to_list[index1] = str(vowels[index2])

    for decoded_chars in str_to_list:
        decoded_str += decoded_chars

    return decoded_str

print(encode("hi there"))
print(decode("h3 th2r2"))