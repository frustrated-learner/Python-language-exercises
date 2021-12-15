# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

# Example :
# "The quick, brown fox jumps over the lazy dog!" = True
# "abcdefghijklmnopqrstuvwxyz" = True
# "Hello World" = False

def is_pangram(s):
    ord_values = []
    sum_to_26 = 351
    ord_sum = 0

    for letters in s.lower():
        if (ord(letters) - 96 >= 1 and (ord(letters) - 96 <= 26)):
            ord_values.append((ord(letters) - 96))

    ord_values = list(set(ord_values))

    for ints in ord_values:
        ord_sum += ints

    return (ord_sum == sum_to_26)

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))