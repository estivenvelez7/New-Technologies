# Realice una FUNCIÓN en Python que calcule el índice de masa corporal de una persona y diga el estado en que se encuentre. Debe recibir los parámetros necesarios.


weightKg = int(input("Enter your weight in Kg (example 76): "))
heightM = float(input("Enter your height in meters (example 1.80):"))

def calculateIMC(weightKg, heightM):
    imc = weightKg / pow(heightM, 2)

    imc = round(imc, 2)

    if imc < 18.5:
        print(f"Your IMC is {imc} and your classification is insufficient")

    if imc >= 18.5 and imc <= 24.9:
        print(f"Your IMC is {imc} and your classification is normal")

    if imc >= 25 and imc <= 26.9:
        print(f"Your IMC is {imc} and your classification is overweight grade 1")

    if imc >= 27 and imc <= 29.9:
        print(f"Your IMC is {imc} and your classification is overweight grade 2 (pre-obesity)")

    if imc >= 30 and imc <= 34.9:
        print(f"Your IMC is {imc} and your classification is obesity type 1")

    if imc >= 35 and imc <= 39.9:
        print(f"Your IMC is {imc} and your classification is obesity type 2")

    if imc >= 40 and imc <= 49.9:
        print(f"Your IMC is {imc} and your classification is obesity type 3 (morbid)")

    if imc > 50:
        print(f"Your IMC is {imc} and your classification is obesity type 4")

    return

calculateIMC(weightKg, heightM)
