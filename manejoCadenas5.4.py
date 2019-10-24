def esLetra(x):
    return (x>='a' and x<='z') or (x>='A' and x<='Z')

def palMayor (pa, pb):
    res = pb
    if len(pa) > len(pb):
        res = pa
    return res

def palMenor (pa, pb):
    res = pb
    if len(pa) < len(pb):
        res = pa
    return res

def palCant (texto):
    pal = ""
    contPal=0
    i=0
    lenTexto = len(texto)
    if lenTexto !=0:
        while i<lenTexto:
            while(i<lenTexto and not (esLetra (texto[i]))):
                i+=1
            j=i
            while(j<lenTexto and esLetra(texto[j])):
                j+=1
            if j!=i:
                contPal +=1
            i=j
    return contPal

def palMayLen(texto):
    pal=""
    palMay=""
    i=0
    lenTexto = len(texto)
    
    if lenTexto!=0:
        while i<lenTexto:
            pal=""
            while(i<lenTexto and not (esLetra(texto[i]))):
                i+=1
            while (i<lenTexto and esLetra(texto[i])):
                pal = pal+texto[i]
                i+=1
            if pal!="":
                if palMay!="":
                    palMay=palMayor(palMay,pal)
                else:
                    palMay = pal
    return palMay

def palMenLen(texto):
    pal=""
    palMen =""
    lenTexto = len(texto)
    i=0
    
    if lenTexto!=0:
        while i < lenTexto:
            pal=""
            while (i<lenTexto and not (esLetra(texto[i]))):
                i+=1
            while (i<lenTexto and esLetra(texto[i])):
                pal = pal + texto[i]
                i+=1
            if pal!="":
                if palMen!="":
                    palMen = palMenor (palMen,pal)
                else:
                    palMen = pal
    return palMen

def main():
    texto = input ("Ingrese el texto: \n")
    cantidad = palCant(texto)
    mayor = palMayLen(texto)
    menor = palMenLen (texto)
    
    print ("El texto tiene", cantidad, " palabras")
    print ("La palabra de mayor longitud es", mayor)
    print ("la palabra de menor longiutd es", menor)
main()

                
                
