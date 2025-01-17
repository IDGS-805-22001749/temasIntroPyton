num1=3
num2=8

'''
relacionales >, <, >=, !=,
aritméticos +, -, *,
boolean or and
'''


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 != num2:
    if num1 > num2:
        print("El valor de {} es mayor que {}".format(num1, num2))
    else: 
        print("El valor de {} es menor que {}".format(num1, num2))
else:
    print("Ambos números son iguales.")
