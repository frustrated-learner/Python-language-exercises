# Write a Python program that takes a list of words and return the longest word and the length of the longest one

list_size = int(input("How many words do you want in the List ? : "))
word_list = []
count = 0
word_length = 0
longest_word = ""

for index in range(list_size):
    words = input(str(f"Enter the Word {index + 1} : "))
    word_list.append(words)

for words in word_list:
    count = len(words)

    if count > word_length: 
        word_length = count
        longest_word = words

print(f"The Longest word is \"{longest_word}\" , Length : {word_length}")

