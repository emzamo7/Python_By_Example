name1 = str(input("type your name: "))
long1 = len(name1)
if long1 <= 5:
    surname1 = str(input("type your surname: "))
    fullname1 = name1 +" "+ surname1
    fullname1 = fullname1.upper() 
    print(fullname1)
else:
    name1 = name1.lower()
    print(name1)
