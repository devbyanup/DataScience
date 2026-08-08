print("Enter a Marks and check how is your performance")
name=input("Enter your name:-")
math=int(input("Enter your marks in maths:-"))
science=int(input("Enter your marks in science:-"))
english=int(input("Enter your marks in english:-"))
social=int(input("Enter your marks in social:-"))
health=int(input("Enter your marks in health:-"))
total=math+science+english+social+health
avg=(total/5)
if avg>=90:
    print(name," is a excellent Student")
elif avg>=80 and avg<=90:
    print(name," is a very good student")
elif avg>=70 and avg<=80:
    print(name," is a good student")
elif avg>=60 and avg<=70:
    print(name," is a good student but need more hard work")
elif avg>=50 and avg<=60:
    print(name," is a above avegrate student")
elif avg>=40 and avg<=50:
    print(name," is a less than average student")
elif avg>=30 and avg<=40:
    print(name," is a bad student")
elif avg>=20 and avg<=30:
    print(name," Try again !!!!")
elif avg>=10 and avg<=20:
    print(name," is a failure student")

