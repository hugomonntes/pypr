import string;
def count_words():
    text = "El gato negro y el gato blanco juegan. El gato negro es rápido."
    counter_words = 0
    words = text.split(" ")
    checkedWords = []
    for word in words:
        wordFormated = word.strip(string.punctuation) #Quito los puntos y simbolos en caso de que esten pegados a la palabra
        if wordFormated.isalpha():
            checkedWords.append(wordFormated)
            if word in words: #FIXME contar cada aparicion de la palabra mas aparecida
                counter_words += 1
    print(checkedWords, counter_words)
        
    
count_words()