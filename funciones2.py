# def conversacion(mensaje):
#     print('hola, como estas')
#     print(mensaje)
#     print('hast pronto')


#     opcion = int(input('Elige una opcion (1, 2, 3): '))
#     if opcion == 1:
#         conversacion('elegiste la opcion 1')
#     elif opcion == 2:
#         conversacion('elegiste la opcion 2')
#     elif opcion == 3:
#         conversacion('elegiste la opcion 3')
#     else:
#         print('elige una opcion, porfavor')

def suma(a, b):
    print('suma d dos numeros')  #funcion para encapsular funciones y reutilizar
    resultado = a + b
    return resultado


numero1 = int(input(' Elige el primer Numeros para sumar: '))
numero2 = int(input(' Elige el segundo Numero par sumar: '))
sumatoria = suma(numero1, numero2)
print(sumatoria)



