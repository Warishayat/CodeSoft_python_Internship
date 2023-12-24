#  Here i will make the ist file with tha name of calculator where i will use of 
#  of diffrent function to perfoam diffrent function like i will make sum,product
#  division and avg and many othe function.
#codsoft____internship_____
import math as mt 
while True:

    def sum(num1,num2):   #function:
        print(f"The Sum of {num1} and {num2} is:",num1+num2)

    def divide(num1,num2): #function2
        print(f"The Division of {num1} and {num2} is:",num1/num2)

    def multiply(num1,num2): #function3
        print(f"The Multiplication of {num1} and {num2} is:",num1*num2)

    def modulus(num1,num2): #function4
        print(f"The Modulus of {num1} and {num2} is:",num1%num2)

    def average(num1,num2): #function5
        print(f"The Average of {num1} and {num2} is:",(num1+num2)/2)

    def sqrt(num1,num2):  #function6
        print(f"The Sqrt of {num1} and {num2} is:",mt.sqrt(num1+num2))
    
    def exponent(num1,num2):    #function7
        #it will take the power of 2 like if we take input 7 and 8 exponent power
        #will be like 2 power 15(7+8).
        print(f"The Exponent of {num1} and {num2} is:",mt.exp2(num1+num2))

    try:
    #take num1 and num2 input from user:
        num1=float(input("Enter the Number1:"))
        num2=float(input("Enter the Number2:"))
    except ValueError:
        print("ValueError: could not convert string to float")
        continue
    #taking operator input from the user
    try:
        operator=int(input("""
        1: for Sum
        2: for Divide
        3: for Multiply
        4: for Modulus
        5: for Average 
        6: for Square-root
        7: for Exponent \n"""))
    except ValueError:
        print("ValueError: could not convert string to float")
        continue
        #now i will check the condition here
    if operator==1:         #Sum
        sum(num1,num2)
    elif operator==2:       #Divide
        divide(num1,num2)
    elif operator==3:       #Multipy
        multiply(num1,num2)
    elif operator==4:       #Modulus
        modulus(num1,num2)
    elif operator==5:       #Average
        average(num1,num2)
    elif operator==6:       #Square-root
        sqrt(num1,num2)
    elif operator==7:       #Exponent
        exponent(num1,num2)
    else:                   #if non from all of above
                print("Invalid-----character")
        
    
    #check again user want to use the calculator:
    try:
        Choiceinput=input("Do you want to continue or close:(y for continue else any number for brake:)")
        if Choiceinput!='y':
            break
        else:
            continue
    except ValueError:
        print("ValueError: could not convert string to float")
        continue

