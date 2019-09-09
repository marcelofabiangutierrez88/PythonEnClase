#def pedirDatos():
#    nro1=int(input("Ingrese numero 1: "))
#    nro2=int(input("Ingrese numero 2: "))
#    leyenda=print ("los resultados para ", nro1, "y para ", nro2, "son: ")
#def opAritmeticaSuma(nro1,nro2):
#    sumar = nro1+nro2
#    print("La Suma: ",sumar)
#    return sumar
#def opAritmeticaResta(nro1,nro2):
#    restar = nro1-nro2
#    print("La resta: ",restar)
#    return restar
#def opAritmeticaMultiplicar(nro1,nro2):
#    multiplicar=nro1*nro2
#    print("La multiplicacion: ",multiplicar)
#    return multiplicar
#def opAritmeticaDividision(nro1,nro2):
#    division=nro1/nro2
#    print("La division: ",division)
#    return division
#def main():
#    pedirDatos()
#    opAritmeticaSuma(10,5)
#    opAritmeticaResta(10,5)
#    opAritmeticaMultiplicar(10,5)
#    opAritmeticaDividision(10,5)
#main()

def main():
    nro1=int(input("Ingrese numero1: "))
    nro2=int(input("ingrese numero2: "))
    print("Los resultados para ",nro1, " y ",nro2," son : ")
    sumar=nro1+nro2
    restar=nro1-nro2
    multiplicar=nro1*nro2
    division=nro1/nro2
    print("La suma: ",sumar)
    print("La resta: ",restar)
    print("La multiplicacion: ",multiplicar)
    print("La division: ",division)
main()