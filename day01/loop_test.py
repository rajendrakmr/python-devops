# Get the env from user and print it

for i in range(1,5):
    env = input("Enter the enviroment: ")  # taking input from user

    if env=='prd':
        print("Don't deploy on friday.")
    elif env =="stg":
        print("Take backup and deploy with test well.")
    else:
        print("Safe to deployment any day.")
    print("The User input Entered env: ",env)

 