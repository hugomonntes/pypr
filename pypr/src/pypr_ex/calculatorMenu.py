def getData():
    return input("Introduce un dato: ")

def showData():
    print(getData())

def isHigher(num1, num2):
    if num1 >= num2:
        return True
    return False

def calculateDivision():
    num1 = getData()
    num2 = getData()
    print(f"Cociente: {num1 / num2}") if isHigher(num1, num2) else print(f"Cociente: {num2 / num1}")
    print(f"Resto: {num1 % num2}") if isHigher(num1, num2) else print(f"Resto: {num2 % num1}")
    print()