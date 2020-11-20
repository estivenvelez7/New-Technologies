# Hacer una actividad que pida al usuario escribir una cantidad X de nombres de personas (puede hacerlo con el ciclo que considere). Después el sistema deberá demostrar cuales son los nombres que empiezan con la letra "C" sea minúscula o mayúscula.

people = input("Enter a person's name (For exit the cycle 0): ")
people_list = []
while people != "0":
    people_list.append(people)
    people = input("Enter a person's name (For exit the cycle 0): ")

for person in people_list:
    if person[0] == 'c' or person[0] == 'C':                
        print(f"The name {person} start with C")
    else:
        print(f"The name {person} not start with C") 
