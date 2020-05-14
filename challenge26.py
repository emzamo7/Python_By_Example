#pig latin

palabra = str(input(" type any word in English: ")) #Solicita cualquier palabra
first = palabra[0] #Ubica el primer espacio de la cadena str
longitud = len(palabra) #Mide la palabra cuantos caracteres

rest = palabra[1:longitud] # los corchetes Evaluan la variable palabra. no toma en cuenta el primer espacio (que es a0), 
#sino que se va a la a1. Toma o substrae  lo que hay del espacio a1 al limite de longitud
#  (len lo contabilizo y se convirtio en un entero) 
if first != "a" and first !="e" and first != "i" and first != "o" and first != "u": #Si la palabra first comienza con
#     alguna vocal
    nuevapalabra = rest + first + "ay" # rest + first + la cadena "ay" dan lugar a la nueva variable
    
else:
    nuevapalabra = palabra + "way" # Si la palabra comienza con vocal, solo se agrega way al final 
print(nuevapalabra.lower())