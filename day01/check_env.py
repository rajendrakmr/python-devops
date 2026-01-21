# Get the env from user and print it

env = input("Enter the enviroment: ")  # taking input from user

if env=='prd':
    print("Don't deploy on friday.")
elif env =="stg":
    print("Take backup and deploy with test well.")
else:
    print("Safe to deployment any day.")
print("The User input Entered env: ",env)


a = int(input("Enter the num 1: "))
b = int(input("Enter the num 2: "))
print(type(a))
print("Multplication is ",a*b)
print("Addition is ",a+b)