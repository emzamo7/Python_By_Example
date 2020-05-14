#demo_list = [1, 'hello', 1.34, True, [1 ,2 , 3]]
colors = ['red', 'green', 'blue']

#number_list = list((1 ,2  , 3 , 4)) # usando constructor : funcion para crear la lista. en este caso: list()
#print(number_list)
#print(type(number_list))

#r = list(range(1 , 1010))
#print(r)
# print(type(colors)) # que tipo de datos es colors
# print(dir(colors)) # Todo lo que puedo hacer con una lista
# print(len(colors))
# print(len(demo_list))

# print(colors[1]) #indices de una lista

#print('green'in colors) # in nos sirve para saber si algo esta en la lista
#print('violet' in colors)

# print(colors)
# colors[1] = 'yellow'
# print(colors)

# print(dir(colors))# viendo los metodos de la lista colors
colors.extend(('violet','dark blue', 'pink', 'black'))
#print(colors)

colors.insert(0, 'gray')
print(colors) 



