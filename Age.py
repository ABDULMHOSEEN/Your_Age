import datetime
print("Hello I am (Age).")
print("My function is to tell your age by taking some information")

def age():
    ynow=datetime.datetime.now().year
    mnow=datetime.datetime.now().month
    dnow=datetime.datetime.now().day
    y=ynow-int(input('inter the year that you was born in'))
    m=(mnow-int(input("inter the month")))*28
    d=dnow-int(input('inter the day'))
    md = ((m+d)//29)
    age=y+(md/10)
    print("your age is {} years and {} months by English calendar".format(y,md))
    x=md+(((10*age)//28))
    if x>12:
        y+1
        x-12
    else:
        y=y
        x=x
    print("your age is {} years and {} months by Arabic calendar".format(y,x))

print(age())


