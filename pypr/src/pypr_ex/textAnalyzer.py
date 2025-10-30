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
            
    for word in checkedWords:
        count = 0
        for w in checkedWords:
            if word == w:
                count += 1
        print(word, "→", count)
        
    
count_words()