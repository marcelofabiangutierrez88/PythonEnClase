def ingresarEnt(msj):
    msj="ingrese numeros o 0(cero) para terminar: "
    print(msj, end="")
    x = int(input())
    return x

def cargarLista(lst):
    i=0
    val=ingresarEnt("["+str(i)+"]:")
    while val!=0:
        lst.append(val)
        val=ingresarEnt("["+str(i)+"]:")
        i+=1
    i+=1
        
def borrarNegativo(lst):
    i=0
    while i < len(lst):
        if lst[i]<0:
            lst.pop(i)
            print("\nError no se pueden ingresar numeros negativos")
        i+=1
        
# def compruebaIguales(lst):  
#     i=0
#     while i< len(lst):
#         if lst[i] in lst:
#             lst.pop(i)
#             i+=1
#             print ("Error no se pueden ingresar numeros iguales")
#         i+=1
        
def main():
    lst=[]
    cargarLista(lst)
    borrarNegativo(lst)
#     compruebaIguales(lst)
    print(lst)
main()
    
    