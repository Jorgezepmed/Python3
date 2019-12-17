#Definicion de lista

nuumeros = [1, 2, 3, 4]
datos = [5, "cadena", 5.5, "texto"]

print(nuumeros)
print(datos)

#Mostar datos por indice 
print(datos[1])

#mostrar datos por Slicing
print(datos[0:2])
print(datos[:-2])

#Mutabilidad

pares = [0, 2, 4, 5, 8, 10]
pares[3] = 6        #Remplaza el valor del lugar tres por un 6 
print (pares)

print("index",pares.index(4))   # Te dice la posicion en la que esta de la lista 


#Funcion de listas
c = len(pares)
pares.append(12)            #append es para agregar otro numero a la "lista"

print('Cantidad de datos', c)
print('Lista actucalizada', pares)