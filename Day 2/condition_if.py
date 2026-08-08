print("This is an example of condition if")

print("Welcome to Abc University")

name = input("Enter your name:- \n")
age = int(input("Enter your age:- \n"))
marks = int(input("Enter your marks:- \n"))
amount = int(input("Enter your amount for admission:- \n"))

if age >= 18:
    print("You are Qualified for entrance exam!!!")

    if marks >= 60:
        print("You are Qualified for admission!!!")

        if amount >= 15000:
            print("Here is your admission bill!!!")
        else:
            print("Sorry, your due amount is left!!!")

    else:
        print("Sorry, you failed!!!")

else:
    print("Sorry, age is not approved for entrance exam!!!")