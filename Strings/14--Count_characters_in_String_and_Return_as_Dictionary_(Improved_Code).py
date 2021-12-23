# Count characters in your string

# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.


def count(string):
    the_dict = {}

    for i in string:
        the_dict[i] = 0;

    the_key_list = list(the_dict.keys())

    for the_keys in the_key_list:
        for letters in string:
            if letters == the_keys:
                the_dict[the_keys] += 1

    return the_dict


print(count('I am a Good Girl'))