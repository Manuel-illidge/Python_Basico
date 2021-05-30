
def conversor(tipo_pesos, valor_dolar):
    pesos_col = input('Cuantos ' + tipo_pesos + ' tienes? ')
    pesos_col = float(pesos_col)

    dolar = pesos_col / valor_dolar
    dolar = round(dolar, 3)
    dolar = str(dolar)

    print('Tienes $' + dolar + ' dolares')


menu = """
Bienvenido al conversor de monedas 💸

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: 
"""
opcion = float(input(menu))

if opcion == 1:
   conversor('Pesos Colombiano', 3879)
elif opcion == 2:
    conversor('Pesos Argentino', 45)
elif opcion == 3:
    conversor('Pesos Mexicanos', 67)
else:
    print('Ingresa una opcion porfavor: ')





