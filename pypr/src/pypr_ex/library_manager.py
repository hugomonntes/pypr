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
    if len(isbn) != 10 or not isbn[0:9].isdigit():
        return False
    if isbn[-1].isdigit() or isbn[-1] == "X":
        return True
    return False

print(isValidIsbn("987_987_98_8X"))

def pide_libro():
    titulo = input("Introduce el titulo del libro: ")
    autor = input("Introduce el autor del libro: ")
    while True:
        isbn = input("Introduce el ISBN del libro: ")
        if isValidIsbn(isbn):
            break
        else:
            print("ISBN no válido. Inténtalo de nuevo.")
    num_paginas = getPositiveNumber()
    return (titulo, autor, isbn, num_paginas)

def main():
    libros = []
    while True:
        print("Menú:")
        print("1. Añadir Libro")
        print("2. Mostrar lista")
        print("3. Eliminar elemento de la lista")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            libro = pide_libro()
            libros.append(libro)
        elif opcion == "2":
            print(f"{'Título'} {'Autor'} {'ISBN'} {'Páginas'}")
            for libro in libros:
                print(f"{libro[0]} {libro[1]} {libro[2]} {libro[3]}")
        elif opcion == "3":
            titulo_eliminar = input("Introduce el título del libro a eliminar: ")
            for libro in libros:
                if libro[0] == titulo_eliminar:
                    libros.remove(libro)
        elif opcion == "4": # TODO falta acabar con archivo
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

main()

# d) En el programa principal crea una lista vacía y luego plantea un menú con las
# opciones:
# Añadir Libro. Pide los datos de un libro y los añade a la lista.
# Mostrar lista: Muestra la lista completa de elementos. Cada campo de un
# libro en una columna distinta. Todo bien alineado.
# Eliminar elemento de la lista. Se elimina por título. Si hay varios con el
# mismo título se eliminan todos.
#  Debe tener persistencia de datos, al final del programa (solo al finalizarlo) guarda
# los datos en un archivo y los lee al volver a ejecutarse.
