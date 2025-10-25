def count_words(text):
    # text = "El gato negro y el gato blanco juegan. El gato negro es rápido."
    words = text.split(" ")
    for i in range (1, words.count() + 1):
        if words.index(i).isalpha():
            words.remove(i)
    print(words)
        
    
count_words("El gato negro y el gato blanco juegan. El gato negro es rápido.")