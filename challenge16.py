raining = str(input("Is it raining?"))
raining = str.lower(raining)

if raining == "yes":
    windy = str(input("Is it windy?"))
    windy = str.lower(windy)
    if windy == "yes":
        print("It's too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("enjoy your day")

    