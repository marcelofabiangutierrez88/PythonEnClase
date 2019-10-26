def fraseParImpar(texto):
    i = 0
    while i < len(texto):
        pal=""
        while i < len(texto) :
            pal = pal + texto[i]
            i+=1
        if len(pal)%2 ==0:
            print("la frase ingresada es par")
        else:
            print("la frase ingresada es impar")
        i+=1
def main():
    texto = input("Ingrese el texto que desea analizar para recibir si es par o impar: ")
    fraseParImpar(texto)
main()