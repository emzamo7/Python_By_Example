answer = str("yes")
count = 0

while answer == "yes":
    name = str(input("Hola. Dime el nombre de alguien que te gustaria que venga a la fiesta: "))
    print(name, "has been invited")
    count = count + 1
    answer = str(input("would you like to invite more people?"))
print("Has invitado", count, "personas")