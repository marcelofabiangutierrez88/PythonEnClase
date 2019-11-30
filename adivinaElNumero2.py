import random

print("Juego adivina el numero. Sin limite de intentos... Se genera un numero entre 1 y 10 ")
nro_secreto=random.randint(1,10)
intentos = int(input("Ingrese numero: "))

while True:
    if intentos == nro_secreto:
        print("Excelente , has ganado!! El numero generado era: \n" , nro_secreto)
        break
    elif intentos < nro_secreto:
        print("Demasiado Bajo\n")
        intentos = int(input("Ingrese numero: "))
    elif intentos>nro_secreto:
        print("Demasiado Alto\n")
        intentos = int(input("Ingrese numero: "))
        