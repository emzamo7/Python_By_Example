

num1 = int(input("how many people do you want in your party?: "))
if num1 < 10:   
    #partynames = str(input("type the names"))
    for i in range(0,num1):
        partynames = str(input("type the name: "))
        print(partynames," has been invited")
else:
    print("too many people")
