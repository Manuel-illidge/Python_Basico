

opcion_menu = int(input("""
Bienvenido a Programas Integrados de Python 💸 

1- numero menos o mayor
2 - Conversor Monedas
3 - 
4 - 

Elige una opcion: 
"""))

if opcion_menu == 1:
        numero = int(input('Escribe un numero: ')) # convertir caracter a entero en una sola linea de codigo

        if numero > 5:
             print('Su numero es mayor a 5')
        elif numero == 5:
            print('Su numero es igual a 5')
        else:
            print('Su numero es menor que 5')


if opcion_menu == 2:

    menu = """
Bienvenido al conversor de monedas 💸 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: 
"""

opcion = float(input(menu))

if opcion == 1:
    pesos_col = input('Ingresa valor en pesos colombianos: ')
    pesos_col = float(pesos_col)

    dolar_valor = 3555
    dolar = pesos_col / dolar_valor
    dolar = round(dolar, 3)
    dolar = str(dolar)

    print('Tienes $' + dolar + ' dolares')

elif opcion == 2:
    pesos_arg = input('Ingresa valor en pesos argentinos: ')
    pesos_arg = float(pesos_arg)

    dolar_valor = 87
    dolar = pesos_arg / dolar_valor
    dolar = round(dolar, 4)
    dolar = str(dolar)

    print('Tienes $' + dolar + ' dolares')

elif opcion == 3:
    pesos_mex = input('Ingresa valor en pesos mexicanos: ')
    pesos_mex = float(pesos_mex)

    dolar_valor = 20
    dolar = pesos_mex / dolar_valor
    dolar = round(dolar, 4)
    dolar = str(dolar)

    print('Tienes $' + dolar + ' dolares')
else:
    print('Ingresa una opcion porfavor: ')
        
        


    



def run():
    pass




if __name__ == '__main__':
    run ()