import math


print("1) Square")
print("2) Triangle")

option = int(input("enter a number: "))
if option == 1:
    base = float(input("type the base"))
    high = float(input("type the high"))
    area = base * high
    print("the area is: ", area)

elif option == 2:

    base = float(input("type the base"))
    high = float(input("type the high"))
    area = (base * high)/2
    print("the area is: ", area)

else:
    print("it's not an option")


