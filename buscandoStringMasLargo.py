def esLetra(x):
    return(x>='a' and x<='z') or (x>='A' and x<='Z')

def encontrandoString(texto):
    i=0
    palMax=""
    while i < len(texto):
        pal=""
        while i < len(texto) and esLetra(texto[i]):
            pal = pal+texto[i]
            i+=1
        if pal!="":
            if palMax!="":
                if len(palMax)<len(pal):
                    palMax=pal
            else:
                palMax=pal
        i+=1
    print("La palabra mas larga es: ",palMax)
def main():
    texto = input("Ingrese string para analizar: ")
    encontrandoString(texto)
main()
            
                