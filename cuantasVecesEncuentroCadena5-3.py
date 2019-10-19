def cadenaEsta(cad,texto):
    i = 0
    cantCoin=0
    lenCad = len(cad)
    lenTexto = len(texto)
    if lenCad !=0 and lenTexto !=0:
        while i <= (lenTexto-lenCad):
            if texto [i:i+lenCad] == cad:
                cantCoin+=1
                i +=lenCad
            else:
                i+=1
    return cantCoin

def main ():
    texto = input ("Ingrese texto largo: \n")
    cad = input ("Ingrese texto corto: \n")
    cantidad = cadenaEsta(cad,texto)
    print ("El texto corto(cad) se encontro ",end="")
    print(cantidad,"veces en el texto largo (texto)")
main()