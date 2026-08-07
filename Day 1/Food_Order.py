print("Welcome to ABC Restaurant")
pizza=550
burger=300
momo=120
print(f"The price of  pizza is : {pizza}")
print(f"The price of  burger is : {burger}")
print(f"The price of  momo is : {momo}")
input("Press any key to continue...")
order=input("Enter your order:")
print(f"Your order is {order}")
if order=="pizza":
    print(f"please pay  :Rs. {pizza}")
if order=="burger":
    print(f"please pay  :Rs. {burger}")
if order=="momo":
    print(f"please pay  :Rs. {momo}")


else:
    print("Sorry, Try Again")


