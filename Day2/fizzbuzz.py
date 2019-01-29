# Day 2 challenge 2 #
letterA = int(input("Enter First number: "))
letterB = int(input("Enter Second number: "))
new =  int(letterA + letterB)

def Cyber(letterA , letterB):
    Cyber(new)


if((new % 5 == 0) and (new % 3 == 0) ):
    print("FIZZBUZZ")
elif(new % 5 == 0):
    print("BUZZ")
elif(new % 3 == 0):
    print("FIZZ")
else:
    print("NOT KNOWN BY THE PROGRAMMER")

