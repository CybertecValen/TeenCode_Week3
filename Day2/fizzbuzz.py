def fizzbuzz(word1,word2):
    words1 = len(word1)
    words2 = len(word2)
    words = words1+ words2

    if( words % 5 == 0 and words % 3 == 0 ):
        print("FIZZBUZZ")
    elif( words % 5 == 0):
        print("BUZZ")
    elif( words % 3 == 0  ):
        print("FIZZ")
    else:
        print("NOT KNOWN THEREFORE ERROR .PLIZ TRY AGAIN.")
    return words


words1 = input("enter string: ")
words2 = input("enter string: ")

print(fizzbuzz(words1,words2))