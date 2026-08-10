attempt=1
while attempt<=5:
    marks=int(input("Enter your marks: "))
    if marks>=60:
        print("You can apply for entrance exam ")
    break
else:
    print("Sorry, you cannot apply for entrance exam ")
    attempt=attempt+1
    if attempt>3:
        attempt=attempt+3




a