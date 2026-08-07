print("Welcome to Calculater")

first_number=int(input("Please enter a first number"))
second_number=int(input("Please enter a second number"))

print("What Operation are you planning to perform?\n type '1' for addition \n '2' for a subtraction \n '3' for multiplication \n '4' for division ")

action=int(input("Please enter your choice"))
if action==1:
    print(first_number+second_number)
if action==2:
    print(first_number-second_number)
if action==3:
    print(first_number*second_number)
if action==4:
    print(first_number/second_number)



