import os

def validar_edad(edad):
    if edad < 1 or edad > 99:
        return False
    return True

while True:
    edad = int(input("Digite Edad "))
    if validar_edad(edad):
        print("Edad Valida")
        break
    else:
        print("Edad no valida")