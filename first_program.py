#A python program Challenege day1 for teencode#

num1 = int( input("Enter current year: "))
num2 = int( input("Enter year of birt") )
num3 = (num1 - num2)


def calc_age(num3):
        if(num3<18):
                print(num3 + "You are a Minor!")
        elif( (num3>=18)and(num3<=36)):
                print(num3 + "You are a Youth!")
        else:
                print(num3 + "You are an elder!")
        










