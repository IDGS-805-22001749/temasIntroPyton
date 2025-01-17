
x = 0

while x <= 10:
    print(x)
    x = x + 1



##Ejercicio pedir un numero y que haga su tabla de multiplicar del 1-10



numero = int(input("Dame el número para hacer su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")



