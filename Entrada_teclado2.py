#Entrada de valores por teclado 


valores = []

c =  int(input("Ingrese la cantidad de valores :"))   #Hacemos que se haga numerica el valore que se ngrese y no como string

for x in range(c):
    valores.append(input("Introduce valor:"))


print(valores)