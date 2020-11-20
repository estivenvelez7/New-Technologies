# Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto, y los devuelva en un diccionario.
print("Enter a phrase: ")
sentence = input()
def countLetters(sentence):
    sentence = sentence.lower().replace(" ", "")
    quantity = dict()
    for x in sentence : 
        if x in quantity:
            quantity[x] += 1
        else: 
            quantity[x] = 1 
    print("This is the number of occurrences that the letter has in the phrase: \n")
    for key, value in quantity.items():
        print(key, ':', value)

print(countLetters(sentence))
