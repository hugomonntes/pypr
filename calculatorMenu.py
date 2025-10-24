def getData():
    return input("Introduce un dato: ")

def showData():
    print(getData())
    
def calculateDivision():
    num1 = getData()
    num2 = getData()
    print(f"La división es: {float(num1) / float(num2)}")
    print(f"Cociente: {float(num1) // float(num2)}")
    print(f"Resto: {float(num1) % float(num2)}")