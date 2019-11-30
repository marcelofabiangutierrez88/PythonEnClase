def leerArchivos():
    arch=open("ejercicio1.txt", "r")
    lineaTot = arch.readlines()
    lstTot=[]
    for linea in lineaTot:
        linea = linea[:-1]
        linea=int(linea)
        lineaTot = linea
        lineaTot=[lineaTot]
        lstTot.append(lineaTot)
        suma=sum(lstTot[0])
        prom=suma/len(lstTot[0])
    arch.close()

    print("Lista extraida del archivo: ",lstTot)
    maximo=max(lstTot)
    minimo=min(lstTot)
    print("promedio",prom)
    print("maximo",maximo)
    print("minimo",minimo)
    print("Lineas totales del archivo",len(lstTot))
    
    
def main():
    leerArchivos()
main()