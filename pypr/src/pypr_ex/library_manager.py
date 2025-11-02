import string
def getPositiveNumber():
    while True:
        try:
            userNum = int(input("Introduce un número positivo: "))
            if userNum > 0:
                return userNum
            else:
                print("El número tiene que ser positivo.")
        except ValueError:
            print("Número no válido")
        
# getPositiveNumber()

def isValidIsbn(isbn: str):
    isbn = isbn.replace(" ", "").replace("_", "")
    if len(isbn) != 10 or not isbn[:9].isdigit():
        return False
    
    if isbn[-1].isdigit() or isbn[-1] == "X":
        return True

    return False

print(isValidIsbn("987_987_98_8X"))

