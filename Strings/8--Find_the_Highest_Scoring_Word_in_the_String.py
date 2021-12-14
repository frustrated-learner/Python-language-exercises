# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

def high(x):
    x = x.split(" ")
    count = 0
    highest = 0
    final_word = ""

    for words in x:
        for letters in words:
            count += ord(letters) - 96
        if count > highest:
            highest = count
            final_word = words
        count = 0

    return final_word

print(high('man i need a taxi up to ubud'))