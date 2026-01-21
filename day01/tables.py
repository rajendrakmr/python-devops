# number = int(input('Input the number you want the table for: '))

# for i in range(1,11):
#     print(f" {number}X{i} = ",number*i)


choice = ""

while choice != "q":
    choice = input("Enter a number for table (or q to quit): ")

    if choice == "q":
        break 
    number = int(choice)

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
