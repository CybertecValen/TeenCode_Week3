#A python program Challenege day1 for teencode#

#code for entering year of birth#

print ("Enter The Current Year")
num1 = int( input("Enter current year: "))


#code for entering current year

print("Enter Your Year Of Birth")
num2 = int( input("Enter year of birth: ") )

#variables years storing the output of num1 and num2

years: int = num1 - num2

#code if statement for varing years#

if(years<18):
        print("YOU ARE A " + str(years) + " " "YEARS OLD")

elif( (years>=18) and (years<=36)):
        print("YOU ARE A " + str(years) + " " "YEARS OLD")

else:
        print("YOUN ARE A" + str(years) + " " "YEARS OLD")






        










