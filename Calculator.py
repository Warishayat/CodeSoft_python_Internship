#  Here i will make the ist file with tha name of calculator where i will use of 
#  of diffrent function to perfoam diffrent function like i will make sum,product
#  division and avg and many othe function.
#codsoft____internship_____
import math as mt 
while True:

    def sum(num1,num2):   #i will make all method inthis fucntion:
        print(f"The Sum of {num1} and {num2} is:",num1+num2)

    def divide(num1,num2):
        print(f"The Division of {num1} and {num2} is:",num1/num2)

    def multiply(num1,num2):
        print(f"The Multiplication of {num1} and {num2} is:",num1*num2)

    def modulus(num1,num2):
        print(f"The Modulus of {num1} and {num2} is:",num1%num2)

    def average(num1,num2):
        print(f"The Average of {num1} and {num2} is:",(num1+num2)/2)

    def sqrt(num1,num2):
        print(f"The Sqrt of {num1} and {num2} is:",mt.sqrt(num1+num2))
    
    def exponent(num1,num2):
        #it will take the power of 2 like if we take input 7 and 8 exponent power
        #will be like 2 power 15(7+8).
        print(f"The Exponent of {num1} and {num2} is:",mt.exp2(num1+num2))


    #pass a num1 and num2:
    num1=float(input("Enter the Number1:"))
    num2=float(input("Enter the Number2:"))
    #pass a operator
    operator=int(input("""
    1: for Sum
    2: for Divide
    3: for Multiply
    4: for Modulus
    5: for Average 
    6: for Square-root
    7: for Exponent \n"""))

    if operator==1:
        sum(num1,num2)
    elif operator==2:
        divide(num1,num2)
    elif operator==3:
       multiply(num1,num2)
    elif operator==4:
        modulus(num1,num2)
    elif operator==5:
        average(num1,num2)
    elif operator==6:
        sqrt(num1,num2)
    elif operator==7:
        exponent(num1,num2)
    else:
        print("Invalid-----character")
    
    Choiceinput=input("Do you want to continue or close:(y for continue else any number for brake:)")
    if Choiceinput!='y':
        break
    else:
        continue

