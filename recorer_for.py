def run():
    nombre = input('Escribe tu Nombre ') #Pedir datos en pantalla
    for letra in nombre:
        print(letra)

    frase = input('Escribir una frase: ')
    for caracter in frase:
        print(caracter.upper)    #cada letra de la palabra en mayuscula en el ciclo


if __name__ == '__main__':
    run()
