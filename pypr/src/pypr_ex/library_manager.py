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
        
getPositiveNumber()

# b) Realiza un función comprueba_isbn a la cual se le pasa un string y hace una
# comprobación sencilla del isbn de 10 digitos teniendo en cuenta las siguientes
# tareas:
# Elimina guiones o espacios si los tuviera.
# El string resultante debe ser de tamaño 10.
# Todos los caracteres son dígitos salvo el último que puede ser dígito o ‘X’.
# Devuelve True o False según sea o no válido el ISBN.
