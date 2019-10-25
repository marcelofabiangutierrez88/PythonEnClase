def histogramas (texto ) :
    aux=""
    contadorCaracter = 0
    x = 0
    for x in texto:
        if x not in aux:
            aux= aux+x
    for caracter1 in aux:
        contadorCaracter =0
        for caracter2 in texto:
            if caracter1 == caracter2:
                contadorCaracter+=1
        print(caracter1, "->",contadorCaracter)
def main():
    histogramas("aabbbbcccdddeee")
main()
