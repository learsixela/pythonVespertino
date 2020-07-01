#solicitar al usuario ingresar un numero y validar si es mayor o menor o igual a cero (0)

x = int(input("Ingrese numero "))

if x == 0:
    print(" es igual a cero")
else:
    if x > 0:
        print(x,"es mayor a cero")
    else:
        print(x,"es menor a cero")

print("***********")

x = int(input("entre: "))
if x<0:
    print("menor a 0")
elif x>0:
    print("mayor a 0")
else:
    print("cero")


print("hacer llamada telefonica")
opcion = input(" contestan llamada [S/N]")
if opcion.upper() == "S":
    opcion2 = input(" quieres merendar conmigo [S/N]")
