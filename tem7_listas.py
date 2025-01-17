#Listas



lista1=[10,5,3]
lista2=[1,5,2,66,1,70,89,2]
lista3=["Lunes","Martes","Miercoles"]
lista4=["Juan", 45, 1.92]
'''
print(type(lista1))
print(len(lista1))

print(lista1[0])

x=0
suma=0
while x<len(lista1):
    suma=suma+lista1[x]
    x=x+1

print("la suma es : {}".format(suma))#???
print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])



lista5=[]

for x in range(5):
    valor=int(input("Ingresa valor:"))
    lista5.append(valor)

print(lista5)


print(lista1)
lista1.pop()
print(lista1)

'''

'''
crea un programa para pedir una catidad n de numeros y almacenarlos en un arreglo, la salida debera ser 
la siguiente:
#Lista completa
#Numeros pares de la lista:
#Numeros impares de la lista:
'''



lista6=[]

n = int(input("Ingrese la cantidad de números: "))

for i in range(n):
    valor = int(input(f"Ingrese el número {i+1}: "))
    lista6.append(valor)



lista1.sort()#ordenar lista
print(lista1)
lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1)#?

