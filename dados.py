#Para este proyecto, tendrás que crear un programa que simule la tirada de dados.

#Cada vez que ejecutamos el programa, éste elegirá dos números aleatorios entre el 1 y el 6.
# El programa deberá imprimirlos en pantalla,
# imprimir su suma y preguntarle al usuario si quiere tirar los dados otra vez.

import random

opcion = ""
while opcion == "":
    print()
    print("******************************************")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print("Dado 1: ", dado1)
    print("Dado 2: ", dado2)

    print("La suma de los dados es : ", dado1 + dado2)
    #falta validar si ingresan una letra o caracter
    opcion=input("Presione Enter si quiere tirar los dados otra vez")

if opcion != "":
    print("***********************")
    print("Juego terminado, adios.")
    print("***********************")
