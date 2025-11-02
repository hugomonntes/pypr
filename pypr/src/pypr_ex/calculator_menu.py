def getData():
     while True:
        try:
            return float(input("Introduce un número: "))
        except Exception:
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
    print(f"Cociente: {num1 // num2:.4f}") if isHigher(num1, num2) else print(f"Cociente: {num2 // num1:.4f}")
    print(f"Resto: {num1 % num2:.4f}") if isHigher(num1, num2) else print(f"Resto: {num2 % num1:.4f}")
    print(f"Division: {num1 / num2:.4f}") if isHigher(num1, num2) else print(f"Cociente: {num2 / num1:.4f}")
    
# calculateDivision()

# Potencia: Pide una base y un exponente, este último será entero.
# Muestra la potencia resultado usando 2 decimales con cadena
# interpolada (f-string).

def calculatePow():
    base = getData()
    exponent = int(getData())
    print(f"Potencia: {base ** exponent:.2f}")
    
# calculatePow()

# Rango: Pide dos números enteros al usuario. Indica cual es el menor y
# cual el mayor. Luego calcula y muestra la suma de todos los números
# entre dichos números (incluyendo ambos números en la suma).

def calculateRangeSum():
    num1 = int(getData())
    num2 = int(getData())
    lower = num1 if num1 < num2 else num2
    higher = num2 if num1 < num2 else num1
    print(f"El menor es: {lower}")
    print(f"El mayor es: {higher}")
    total_sum = 0
    for i in range(lower, higher + 1): # Sumo porque el final no esta incluido en el rango
        total_sum += i
    print(f"Suma de todos los números entre {lower} y {higher}: {total_sum}")
    
# calculateRangeSum()

# Listas: Pide al usuario un tamaño para la lista. Crea dos listas de
# números aleatorios (en el rango que tu quieras) del tamaño indicado
# por el usuario. Finalmente muestra las dos listas y una tercera que
# incluya la suma elemento a elemento de ambas listas.

def calculateListSum():
    list_size = int(getData())
    import random
    list = []
    list2 = []
    sum_total = 0
    for i in range(1, list_size + 1):
        list.append(random.randint(1, 20))
        list2.append(random.randint(1, 20))
        sum_total += list[i - 1] + list2[i - 1]
    print(list)
    print(list2)
    print(f"Suma total: {sum_total}")
    
calculateListSum()