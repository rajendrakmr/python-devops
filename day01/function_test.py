# Scripting  = Set of instructions
# Functions Example 

def sum_of_num():
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    
    sum = num1 + num2
    print("Sum of num1 and num2 : ",sum)


env = input("Enter the User Enviroment: ")
if env =="prd":
    sum_of_num()
print("Entered the User Enviroment is ",env)