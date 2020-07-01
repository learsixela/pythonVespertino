
def saludo():
    print("saludo")
saludo()

def mensaje():
    print("Hola clase")
    print("Hola clase2")
    print("Hola clase3")
mensaje()

saludo()
print("mensaje fuera de funcion")
mensaje()

numero2 =6
#numero1 = 5
def suma():
    print(numero1+numero2)

print("dfsgsfdgh")
#input("kjdsñlaih")
#las variables a utilizar en la funcion deben ser declaradas o
#dentro de la funcion o antes del llamado de la función
numero1 = 4
#llamado a la funcion
suma()

numero1 = 7
print(numero1*numero2)
numero1 = int(input("ingrese numero 1 "))
numero2 = int(input("ingrese numero 2 "))

#crear una funcion que recibe parametros o variables
def multiplicacion():
    print("el resultado de la multiplicacion 1 es ",numero1*numero2)
multiplicacion()

def multiplicacion(num1, num2):
    print("el resultado de la multiplicacion 2 es ",num1*num2)
multiplicacion(numero1,numero2)

def resta(num1, num2):
    print("la resta es: ",num1-num2 )
#pasasando variables con valor predefinido, deben llamarse igual
resta(num1=7, num2=4)

#funcion que retorna un resultado
def division (num1, num2):
    if(num2 != 0):
        print("impresion dentro de la funcion : la división es: ", num1 / num2)
        resultado = num1 / num2
        return resultado
    else:
        print("impresion dentro de la funcion : No se puede dividir por cero")
        mensaje = "No se puede dividir por cero "
        return mensaje

print('valor retornado es ',division(numero1,numero2))

# podemos almacenar el retorno de la funcion
resultado_division = division(numero1,numero2)

if(resultado_division >0):
    print(' el resultado es mayor a cero:',resultado_division)

    # variables por referencia y variables por valor