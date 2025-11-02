import string;
def contar_palabras():
    text = "El gato negro y el gato blanco juegan. El gato negro es rápido."
    words = text.split(" ")
    checkedWords = []
    for word in words:
        wordFormated = word.strip(string.punctuation) #Quito los puntos y simbolos en caso de que esten pegados a la palabra y lo pongo en minuscula
        if wordFormated.isalpha():
            checkedWords.append(wordFormated)
    
    wordPerAppearances = {}
    for word in checkedWords:
        if word in wordPerAppearances:
            wordPerAppearances[word] += 1
        else:
            wordPerAppearances[word] = 1
    return wordPerAppearances
    
contar_palabras()

def estadisticas_texto(text: string):
    return (len(text), )

def calcular_logitudMedia_palabras(words: dict):
    palabras = list(words.keys())
    for palabra in palabras:
        tamaños = [len(palabra)]
    print(tamaños)

calcular_logitudMedia_palabras(contar_palabras())

def main():
    fileName = input("Introduce el nombre del archivo: ")
    print(contar_palabras())
    
# b) Función estadisticas_texto: Recibe un texto y devuelve en una tupla:
# • Número total de palabras.
# • Longitud media de las palabras.
# • Palabra más larga.
# • Palabra más frecuente.

# c) Programa principal: Pide el nombre de un archivo de texto al usuario y muestra
# primero el diccionario que devuelve contar_palabras y luego las estadísticas que
# devuelva estadisticas_texto. Presenta todos los datos de forma adecuada y bien
# alineados. 