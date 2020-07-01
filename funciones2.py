#listas
#conjunto de datos, ordenados segun su ingreso, separados por "coma"
lista_numeros = [1,2,3,4,5,6,7,8,9,0]
print(lista_numeros)

#las listas comienzan en la posicion cero (indice)
lista_distintos_datos = ["uno",2, "tres",4] #-4, -3,-2, -1 ,0,1,2,3
print(lista_distintos_datos)

#acceder a un dato de la lista
print(lista_distintos_datos[0])
print(lista_distintos_datos[-4])

#imprimir para acceder desde un indice o posición
print(" desde indice 1: ",lista_distintos_datos[1:]) #[2, 'tres', 4]

#suma de listas (concatenar listas)
lista_uno = [1,2,3,4]
lista_dos = [5,6,7,8]
lista_tres = lista_uno+lista_dos
print("suma de listas ",lista_tres) #[1, 2, 3, 4, 5, 6, 7, 8]

#reemplazando el contenido en una posicion
#MUTABILIDAD
lista_tres[4] =9 #5 ->9 [1, 2, 3, 4, 9, 6, 7, 8]
print("suma de listas 2 ",lista_tres)

#agregar nuevo contenido a la lista con append()
lista_tres.append(5)
print("suma de listas 3 ",lista_tres) #[1, 2, 3, 4, 9, 6, 7, 8, 5]

lista_tres.append("0")
print("suma de listas 4 ",lista_tres) #[1, 2, 3, 4, 9, 6, 7, 8, 5, '0']
print("contenido : ",lista_tres[9])

print("Imprimir los primeros X valores",lista_tres[:5]) # [1, 2, 3, 4, 9]

lista_tres[:5] = ['a']
print("nueva lista 3",lista_tres) #['a', 6, 7, 8, 5, '0']

#tamaño de la lista
print("Len : ",len(lista_tres))

#ddejar lista vacia
lista_tres = []
print(lista_tres)