print("Enter a week day to check weekend or not ")
print("We are using OR condition")
day=int(input("Type 1 for Sunday \n Type 2 for Monday \n Type 3 for Tuesday \n Type 4 for Wednesday \n Type 5 for Thursday \n Type 6 for Friday \n Type 7 for Saturday \n "))
if day==1 or day==7:
    print("Its a weekend. Enjoy ")
else:
    print("Its not  weekend bro ")

