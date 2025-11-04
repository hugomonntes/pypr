import string

def contar_palabras():
    text = "El gato negro y el gato blanco juegan. El gato negro es rápido."
    words = text.split()
    checkedWords = []

    for word in words:
        wordFormated = word.strip(string.punctuation).lower()
        if wordFormated.isalpha():
            checkedWords.append(wordFormated)
    
    wordPerAppearances = {}
    for word in checkedWords:
        if word in wordPerAppearances:
            wordPerAppearances[word] += 1
        else:
            wordPerAppearances[word] = 1
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
    diccionario = contar_palabras()
    total_palabras = len(diccionario)
    longitud_media = calcular_longitudMedia_palabras(diccionario)
    palabra_larga = palabra_mas_larga(diccionario)
    palabra_frecuente = max(diccionario, key=diccionario.get)
    
    return (total_palabras, longitud_media, palabra_larga, palabra_frecuente)

def main():
    print(estadisticas_texto("El gato negro y el gato blanco juegan. El gato negro es rápido."))

main()
# b) Función estadisticas_texto: Recibe un texto y devuelve en una tupla:
# • Número total de palabras.
# • Longitud media de las palabras.
# • Palabra más larga.
# • Palabra más frecuente.

# c) Programa principal: Pide el nombre de un archivo de texto al usuario y muestra
# primero el diccionario que devuelve contar_palabras y luego las estadísticas que
# devuelva estadisticas_texto. Presenta todos los datos de forma adecuada y bien
# alineados. 