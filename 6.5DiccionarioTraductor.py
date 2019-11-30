def agregarDicEle(dic):
    i=0
    dic={}
    continua="s"
    while continua =="s":
        x=int(input("Ingrese clave: "))
        y=str(input("Ingrese valor: "))
        dic[x]=y
        print(dic)
        continua=input("Desea cargar otro dato al diccionario[s/n]?")
        print(dic)
    z=int(input("Ingresar un numero para traducir o cero para salir: "))
    if z!=0:
        if z not in dic:
            print()
            z=int(input("Error: Ingresar un numero para traducir o cero para salir: "))
            dic2=dic.get(z)
            print(z,'->',dic2)
        else:
            dic2=dic.get(z)
            print(z,'->',dic2)
def main():
    dic={}
    agregarDicEle(dic)
main()
    
    
    
    