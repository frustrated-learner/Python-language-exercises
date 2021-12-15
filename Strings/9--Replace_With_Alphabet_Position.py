# Welcome.

# In this Problem you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example :

# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

def alphabet_position(text):
    str_ls = []
    ans = ""

    for strings in text.lower():
        if (ord(strings) - 96) >= 1 and (ord(strings) - 96) <= 26:
            str_ls.append(str(ord(strings) - 96))
           
    ans = " ".join(str_ls) 

    return ans

print(alphabet_position("The sunset sets at twelve o' clock."))