from random import randint
import random

def azar(inf,sup):
    return randint(inf,sup)

def cargarListaAle(lst,cant,inf,sup):
    i=0
    val=azar(inf,sup)
    while i<cant:
        if val not in lst:
            lst.append(val)
            val=azar(inf,sup)
            i+=1
        i+=1
    return lst

        
def sumaListas(lst,lst2):
    lstUnion=[]
    for i in lst:
        if i not in lstUnion:
            lstUnion.append(i)
    for i in lst2:
        if i not in lstUnion:
            lstUnion.append(i)
    return lstUnion

def interseccion(lst,lst2):
    lstIn=[]
    lstIn=(set(lst) & set(lst2))
    return lstIn

def diferencia(lst,lst2):
    lstDif=[]
    lstDif=(set(lst2)-set(lst))
    return lstDif

def diferenciaSimetrica(lst,lst2):
    lstDifSi=[]
    lstDifSi=(set(lst)^ set(lst2))
    return lstDifSi


def main():
    opcion=0
    lst=[]
    lst2=[]
    cargarListaAle(lst,8,0,20)
    cargarListaAle(lst2,8,0,20)
  
    while opcion!=6: 
        print("1. CARGAR CONJUNTOS:")
        print("2. UNION: ")
        print("3. INTERSECCION: ")
        print("4. DIFERENCIA(A-B): ")
        print("5. DIFERENCIA SIMETRICA: ")
        print("6. SALIR: \n")
        
        print("Eliga la opcion deseada: " )
        opcion = int(input())
        if opcion==1:
            print("Lista 1:",lst)
            print("Lista 2:",lst2)
            print()
        if opcion ==2:
            union=sumaListas(lst,lst2)
            print("Union: \n",union)
            print()
        if opcion ==3:
            inter=interseccion(lst,lst2)
            print("Interseccion: ",inter)
            print()
        if opcion ==4:
            dif=diferencia(lst,lst2)
            print("Diferencia: ",dif)
            print()
        if opcion ==5:
            difSim=diferenciaSimetrica(lst,lst2)
            print("Diferencia Simetrica: ", difSim)
            print()
        if opcion ==6:
            print("Gracias...")
        

        
    
#     lst=[]
#     lst2=[]
#     cargarListaAle(lst,8,0,20)
#     cargarListaAle(lst2,8,0,20)
#     print("Lista Original:",lst)
#     print("Lista Original:",lst2)
#     union=sumaListas(lst,lst2)
#     print("Union: ",union)
#     inter=interseccion(lst,lst2)
#     print("Interseccion: ",inter)
#     dif=diferencia(lst,lst2)
#     print("Diferencia: ",dif)
#     difSim=diferenciaSimetrica(lst,lst2)
#     print("Diferencia Simetrica: ", difSim)

main()