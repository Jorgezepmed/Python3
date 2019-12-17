#Test while

opcion = 0 

while opcion <10:
    
    opcion += 1
    if opcion == 5:
        print('Estas en el ', opcion)
        continue
    print(opcion)

    if opcion == 7:
        break

else:
    print('Termino el siclo while')