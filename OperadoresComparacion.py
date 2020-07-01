#if: else:

numero1 = input("ingrese numero 1")#7
numero1 = int(numero1)

numeros2= int(input("ingrese numero 2"))#8

if numero1 == numeros2:
    print("Los numeros son iguales")
elif numero1 > numeros2:
    print('El numero mayor es el primer numero',numero1)
else: #numeros2 > numero1
    print('El numero mayor es el segundo numero', numeros2)

print("****************")

if numero1 == numeros2:
    print("Los numeros son iguales")
else:
    if numero1 > numeros2:
        print('El numero mayor es el primer numero',numero1)
    else:
        print('El numero mayor es el segundo numero', numeros2)

