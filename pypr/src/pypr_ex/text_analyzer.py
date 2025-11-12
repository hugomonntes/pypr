import string

def contar_palabras(text):
    words = text.split()
    checkedWords = []

    for word in words:
        wordFormated = word.strip(string.punctuation).lower()
        if wordFormated.isalpha():
            checkedWords.append(wordFormated)
    
    wordPerAppearances = {}
    for word in checkedWords:
        wordPerAppearances[word] = (wordPerAppearances[word] | 0) + 1 
    return wordPerAppearances

def calcular_longitudMedia_palabras(words: dict):
    longitudes = []
    for palabra in words.keys():
        longitudes.append(len(palabra))
    
    suma = 0
    for longitud in longitudes:
        suma += longitud
    
    return suma / len(longitudes)

def palabra_mas_larga(diccionario: dict):
    return max(diccionario.keys(), key=len)

def estadisticas_texto(text: str):
    diccionario = contar_palabras(text)
    total_palabras = len(diccionario)
    longitud_media = calcular_longitudMedia_palabras(diccionario)
    palabra_larga = palabra_mas_larga(diccionario)
    palabra_frecuente = max(diccionario, key=diccionario.get)
    
    return (total_palabras, longitud_media, palabra_larga, palabra_frecuente)

def main():
    while True:
        nombre_archivo = input("Introduce el nombre del archivo de texto: ")
        try:
            with open(nombre_archivo, "r") as file:
                texto = file.read()
                break
        except FileNotFoundError:
            print("No se encuentra el archivo.")

    diccionario = contar_palabras(texto)
    print("Diccionario de palabras y frecuencia:")
    for palabra, frecuencia in diccionario.items():
        print(f"{palabra:<12} : {frecuencia}")
    total, media, larga, frecuente = estadisticas_texto(texto)
    print(f"{'Total de palabras únicas:':30} {total}")
    print(f"{'Longitud media de palabras:':30} {media:.2f}")
    print(f"{'Palabra más larga:':30} {larga}")
    print(f"{'Palabra más frecuente:':30} {frecuente}")

main()