import random
print("Welcome to Gold City ")
Adv=["left","right"]
advs=random.choice(Adv)
type=input("Where do you want to step : Left or Right?").lower()
print(type)
if type==advs:
    print("You found gold")
else:
    print("You are caught")

