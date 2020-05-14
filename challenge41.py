name = input("type your name: ")
number = int(input("type a number: "))
if number < 10:
    for i in range(0,number):
        print(name)
else:
    print("too high")