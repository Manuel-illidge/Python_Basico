def conversacion(mensaje):
    print('hola, como estas')
    print(mensaje)
    print('hasta pronto')
    


    opcion = int(input('Elige una opcion 1,2,3: '))
    if opcion == 1:
        conversacion('Elegistela opcion 1')
    elif opcion == 2:
        conversacion('elegiste la opcion 2')
    elif opcion == 3:
        conversacion('elegiste la opcion 3')
    else:
        print('elige una opcion, porfavor')

