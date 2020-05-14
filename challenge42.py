total = 0

for i in range(0,5):
    num = int(input("dame un numero: "))
    ans = input("quieres este numero incluido? si o no: ")
    if ans == "si":
        total = total + num
print(total)
