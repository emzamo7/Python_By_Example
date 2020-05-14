compnum = 50
guess = int(input("Can you guess a number I am thinking off? "))
count = 1
while guess != compnum:
    if guess < compnum:
        print("Low")
    else:
        print("high")
    count = count + 1
    guess = int(input("have another guess: "))
print("Well done, you took", count, "attempts")