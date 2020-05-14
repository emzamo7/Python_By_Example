num = int(input("enter a number between 10 and 20: "))
while num < 10 or num > 20:
    if num < 10:
        print("low")
    else:
        print("high")
    num = int(input("try again"))
print("thx")