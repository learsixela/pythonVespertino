def funcionFor():
    print("funcion for")
    #for variable in elemento iterable (lista) :
    for i in "TEMUCO":
        print("i: ",i)
        print(f" dentro de for {i}")

#creamos una lista
lista_uno = ['a', 'b', 'c', 'd']
#llamado a la funcion
funcionFor()

var= int(input("cual es la cantidad de veces"))
for i in range(var):
    print("i en range 7: ", i)

for i in range(1,10):
    print("i en range 1 al 9: ", i)

var1= int(input("tamaño de la lista?")) # cantidad del range
lista = [] #definir lista vacia
contador = 0 #inicializar contador en cero
for x in range(var1):
    print(" x ", x,"contador",contador)
    #lista[contador] = 1+contador #asignacion, reemplazando el valor
    contador = 1 + contador #incremento del contador
    lista.append(contador) #agregando contenido a la lista

print("tamaño lista es : ",len(lista)) #tamaño de la lista


print("********************")


#crear una lista con los 5 primeros numeros pares

lista_numeros_pares=[]
lista_numeros_impares=[]
#for variable in elemento iterable (range) :
for i in range(1,11):
    if(i%2 ==0):
        lista_numeros_pares.append(i)
    else:
        lista_numeros_impares.append(i)

print("numeros pares: ",lista_numeros_pares)
print("numeros impares: ",lista_numeros_impares)