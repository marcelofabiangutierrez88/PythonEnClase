def esLetra(x):
    return (x>='a' and x<='z') or (x>='A' and x<='Z')

def esPalindroma(texto):
    textoLim=""
    for c in texto:
        if esLetra(c):
            textoLim=textoLim +c
    return textoLim==textoLim[::-1]
def main():
    texto = "somos o no somos"
    if esPalindroma(texto):
        print(texto,"\n***Es Palindromo")
    else:
        print(texto,"\*** No es Palindromo")
main()
    