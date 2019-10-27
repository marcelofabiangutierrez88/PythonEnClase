def esLetra(x):
    return (x>='a' and x<='z') or (x>='A' and x<='Z')

def minuscula1(x):
    res=x
    if x>='A' and x<='Z':
        res=chr(ord(x)+32)
    return res

def minuscula2(xs):
    res=""
    for x in xs:
        res = res + minuscula1(x)
    return res

def carMin(texto):
    contadorCar = 0
    caracterMinimo=""
    contadorCaracterMinimo=0
    for caracter1 in texto:
        contadorCar= 0
        for caracter2 in texto:
            if caracter1 ==caracter2:
                contadorCar+=1
        if caracterMinimo!="":
            if contadorCaracterMinimo>contadorCar:
                contadorCaracterMinimo=contadorCar
                caracterMinimo=caracter1
        else:
            contadorCaracterMinimo = contadorCar
            caracterMinimo = caracter1
    print("El caracter que menos se repite /en la cadena es: ",minuscula2(caracterMinimo), '->', contadorCaracterMinimo,"vez/veces repetido\n")
    
def esPalindroma(texto):
    textoLim=""
    for c in texto:
        if esLetra(c):
            textoLim=textoLim+c
    return minuscula2(textoLim)==minuscula2(textoLim[::-1])

def histogramas(texto):
    aux=""
    contadorCaracter=0
    x = 0
    for x in texto:
        if x not in aux:
            aux = aux+x
    for caracter1 in aux:
        contadorCaracter =0
        for caracter2 in texto:
            if esLetra(caracter1) == esLetra(caracter2):
                contadorCaracter +=1
        print("Histograma","Caracter",caracter1,'->' ,contadorCaracter,"vez/veces repetido\n" )
        
def cadenaPar(texto):
    i=0
    while i <len(texto):
        pal=""
        while i <len(texto) and esLetra(texto[i]):
            pal = pal + texto[i]
            i+=1
        if len(pal)%2 ==0:
            print("la frase ingresada es Par, longitud de: ",len(pal))
        else:
            print("la frase ingresada es Impar, longitud de: ",len(pal))
        i+=1

def palabraCorta(texto):
    i = 0
    palMin=""
    while i < len(texto):
        pal = ""
        while i<len(texto) and esLetra(texto[i]):
            pal = pal + texto[i]
            i+=1
        if pal!="":
            if palMin!="":
                if len(palMin)>len(pal):
                    palMin= pal
            else:
                palMin = pal
        i+=1
    print("La palabra mas corta es: ", palMin, "\n")
    
def vocales(texto):
    aux=""
    vocal="aeiou"
    for x in texto:
        if x in vocal:
            aux=aux+x
    for car1 in vocal:
        conCar=0
        for car2 in aux:
            if car1==car2:
                conCar+=1
        print("Vocal: ",car1,'->', conCar,"vez/veces repetido")
                   
def main():
    texto = input("Ingrese texto a analizar: ")
    carMin(texto)
    if esPalindroma(texto):
        print("La cadena ingresada es Palindroma!!\n")
    else:
        print("La cadena ingresada No es Palindroma!!\n")
    histogramas(texto)
    cadenaPar(texto)
    palabraCorta(texto)
    vocales(texto)
main()


    