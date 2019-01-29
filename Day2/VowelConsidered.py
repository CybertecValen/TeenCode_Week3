# Function that takes a string and returns a tuple containing a ..... #
# output will be lyk#
# valen -> vln ae #

def considered(word):
    consonants = ''
    vowels = ''
    for valen in range(0, len(word)):
        letter = word[valen]
        if letter in 'aeiou':
            vowels += letter
        else:
            consonants += letter
    return consonants + '  ' + vowels


while True:
    word = input("Enter words only: ")
    if word == "exit":
        break
    print("Considered: ", considered(word))
