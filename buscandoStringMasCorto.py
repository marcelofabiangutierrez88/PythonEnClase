def esLetra(x):
    return (x>='a' and x<='z') or (x>='A' and x<='Z')
def palabraCorta(texto):
    i=0
    palMin =""
    while i < len(texto):
        pal=""
        while i<len(texto) and esLetra(texto[i]):
            pal = pal +texto[i]
            i+=1
        if pal!="":
            if palMin!="":
                if len(palMin) > len(pal):
                    palMin = pal
            else:
                palMin=pal
        i+=1
    print("La palabra mas corta analizada es: ",palMin)
def main():
    texto = input("Ingrese cadena a analizar el texto mas corto: ")
    palabraCorta(texto)
main()