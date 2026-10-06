with open("data.txt", "r") as file:
    data = file.read()

word_to_find = input("Enter the word to find:  ")
replacement_word = input('Enter the replacement word:')

modified_data = data.replace(word_to_find, replacement_word)

with open("data.txt", "w") as file:
    file.write(modified_data)
