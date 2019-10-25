def esLetra(x):
    return (x>='a' and x<='z') or (x>='A' and x<='Z')

def minimoCaracterRepetido(texto):
    contadorCar = 0
    caracterMinimo =""
    contadorCaracterMinimo = 0
    for caracter1 in texto:
        contadorCar=0
        for caracter2 in texto:
            
            if caracter1==caracter2:
                contadorCar +=1
        if caracterMinimo !="":
            if contadorCaracterMinimo>      contadorCar:
                contadorCaracterMinimo = contadorCar
                caracterMinimo = caracter1
        else:
            contadorCaracterMinimo = contadorCar
            caracterMinimo = caracter1
    print(caracterMinimo, "->",contadorCaracterMinimo)
def main():
    minimoCaracterRepetido("hhooolllla0")
main()
