myStr = "Emmanuel"

print("My name is " + myStr) #Concatenacion
print(f"My name is {myStr} ") #en vez de concatenarlo, usamos f para decir que el myStr tiene que ser interpretado como una variable de arriba , creado anteriormente
print("My name is {0}".format(myStr)) #format es tipico en python. solo se pone 0 entre las llaves


#print(dir(myStr))

# print(myStr.upper()) # todo mayuscula - metodo upper
# print(myStr.lower()) # todo minuscula - metodo lower
# print(myStr.swapcase()) # convierte una letra mayuscula otra minuscula
# print(myStr.capitalize()) # metodo capitalize - primera letra a mayuscula

# print(myStr.replace('Hello','bye').upper()) # reemplaza txt : en vez de hello, bye

# print(myStr.count(' '))

# print(myStr.startswith('Hello')) # Busca por caracteres. Son metodos.

# print(myStr.endswith('World'))
# print(myStr.split(','))
# print(myStr.find('o'))
# print(len(myStr))
# print(myStr.index('e'))

# print(myStr.isnumeric())
# print(myStr.isalpha())
# print(myStr.isascii())

# print(myStr[0])
# print(myStr[3])
# print(myStr[-1])
# print(myStr[-5])
# print(myStr[-2])
# print(myStr[-3])