print("Nos fuimos a cenar N personas. Nos llega la cuenta y la vamos a dividir entre todos. Cuanto tenemos que pagar por cada uno?")
dinners = int(input("cuantas personas vinieron?"))
totalCuenta = float(input("de cuanto es la cuenta?"))

totalPagar = totalCuenta / dinners
print("Cada uno pagara : ",totalPagar, "pesos")