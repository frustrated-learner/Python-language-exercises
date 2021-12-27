# Reverse every other word in the string

# Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this Question.

# Example:
# "Did it work?"                         => "Did ti work?"
# "I really hope it works this time..."  => "I yllaer hope ti works siht time..."
# "Reverse this string, please!"         => "Reverse siht string, !esaelp"
# "Have a beer"                          => "Have a beer"
# ""                                     => ""

def reverse_alternate(string):
    word_list = ' '.join(string.split())
    word_list = word_list.split(" ")

    for index, words in enumerate(word_list):
        if (index + 1) % 2 == 0:
            word_list[index] = "".join((list(reversed(words))))

    final_answer = " ".join(word_list)

    return final_answer

print(reverse_alternate("I really hope it works this time..."))