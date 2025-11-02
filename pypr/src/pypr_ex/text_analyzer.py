import string;
def count_words():
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
    print(wordPerAppearances)
    
count_words()