# Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
Cword = input("Write a text:")
Cword = Cword.lower()
words = Cword.split(" ")
dict = {}

for p in words:
    if p in dict:
        dict [p] += 1
    else:
        dict [p] = 1

for field,value in dict.items():
    print(f"The word was found '{field}': {value} times")


# go to the nasa 