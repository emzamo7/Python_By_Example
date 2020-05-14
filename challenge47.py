num1 = 0
total = 0
answer = "y"

num1 = int(input("enter a number: "))
total = num1

while answer == "y":
    
    
    num2 = int(input("enter another number: "))
    
    total = num2 + total
    answer = input("would you want to add another numbr?: ")

print(total)
