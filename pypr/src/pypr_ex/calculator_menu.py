import random

def getData():
    while True:
        try:
            return float(input("Introduce un número: "))
        except ValueError:
            print("Error! introduce un número válido.")

def showData():
    print(getData())

def isHigher(num1, num2):
    return num1 >= num2

def calculateDivision():
    num1 = getData()
    num2 = getData()
    if num2 == 0 or num1 == 0:
        print("Error! División por cero no está permitida.")
        return
    if isHigher(num1, num2):
        print(f"Cociente (entero): {num1 // num2:.4f}")
        print(f"Resto: {num1 % num2:.4f}")
        print(f"División (decimal): {num1 / num2:.4f}")
    else:
        print(f"Cociente (entero): {num2 // num1:.4f}")
        print(f"Resto: {num2 % num1:.4f}")
        print(f"División (decimal): {num2 / num1:.4f}")

def calculatePow():
    base = getData()
    exponent = int(getData())
    print(f"Potencia: {base ** exponent:.2f}")

def calculateRangeSum():
    num1 = int(getData())
    num2 = int(getData())
    lower = num1 if num1 < num2 else num2
    higher = num2 if num1 < num2 else num1
    print(f"El menor es: {lower}")
    print(f"El mayor es: {higher}")
    total_sum = 0
    for i in range(lower, higher + 1):
        total_sum += i
    print(f"Suma de todos los números entre {lower} y {higher}: {total_sum}")

def calculateListSum():
    list_size = int(getData())
    list1 = []
    list2 = []
    list_sum = []
    for i in range(list_size):
        list1.append(random.randint(1, 20))
        list2.append(random.randint(1, 20))
        list_sum.append(list1[i] + list2[i])
    print("Lista 1:", list1)
    print("Lista 2:", list2)
    print("Suma elemento a elemento:", list_sum)


def menu():
    while True:
        print("1. Divisiones")
        print("2. Potencia")
        print("3. Rango")
        print("4. Listas")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            calculateDivision()
        elif opcion == "2":
            calculatePow()
        elif opcion == "3":
            calculateRangeSum()
        elif opcion == "4":
            calculateListSum()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

menu()