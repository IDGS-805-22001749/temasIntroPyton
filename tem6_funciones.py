import os

def funcion1():
    os.system('cls') 
    print("Hola, soy la función 1")
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    res = num1 + num2
    print("El resultado de la suma es:", res)  
    return res  

def funcion2():
    print("Hola, soy la función 2")

def run():
    os.system('cls')
    print("Menú de opciones:")
    print("1. Suma de dos números")
    print("2. Otra opción")
    print("3. Salir")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        funcion1()
    elif opcion == 2:
        funcion2()
    elif opcion == 3:
        print("Saliendo del programa...")
        exit()  
    else:
        print("Opción inválida")

if __name__ == "__main__":
    run()