# In this Question, you've to count lowercase letters in a given string and return the letter count in a hash with 'letter' as key and count as 'value'. The key must be 'symbol' instead of string in Ruby and 'char' instead of string in Crystal.

# Example:

# letter_count('arithmetics') #=> {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}

def letter_count(s):
    str_to_ls = []
    sorted_2d_arr = []
    arr_2d_index = 0

    count = 0

    for letters in s:
        str_to_ls.append(letters)

    str_to_ls.sort()

    sorted_ls = list(set(str_to_ls))
    sorted_ls.sort()

    for sorted_letters in sorted_ls:
        sorted_2d_arr.append([sorted_letters])

    for letters_2 in sorted_ls:
        for letters_3 in str_to_ls:
            if letters_3 == letters_2:
                count += 1
                
        sorted_2d_arr[arr_2d_index].append(count)
        arr_2d_index += 1
        count = 0


    return dict(sorted_2d_arr)

print(letter_count('arithmetics'))