
direction = str(input("which direction do you want?up or down?: "))
direction = direction.lower()
if (direction == "up") :
    topNumber= int(input("type a top number: "))
    for i in range(1,topNumber+1,+1):
        print(i)
elif (direction == "down"):
    downnumber = int(input("please, enter a number below 20: "))
    for i in range(20,downnumber-1,-1):
        print(i)
else:
    print("I don't understand")

