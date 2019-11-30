def agregarDicEle2(dic):
    i=0
    dic={}
    continua="s"
    while continua =="s":
        x=int(input("Ingrese clave: "))
        y=str(input("Idioma Español(sp): "))
        z=str(input("Idioma Ingles(en): "))
        w=str(input("Idioma Aleman (de): "))
        dic[x]=y,z,w
        continua=input("Desea cargar otro dato al diccionario[s/n]?")
        tupla=(y,z,w)
        print(dic)
        
    z=int(input("Ingresar un numero para traducir o cero para salir: "))
    if z!=0:
        e="sp"
        i="en"
        a="de"
        if z not in dic:
            print()
            z=int(input("Error: Ingresar un numero para traducir o cero para salir: "))
            t=str(input("Ingrese idioma ['en'|'sp'|'de']: "))
            if t != e or t!=i or t!=a:
                t=str(input("Error, Ingrese un idioma para traducir['en'|'sp'|'de']: "))
            else:
                 t=str(input("Ingrese idioma ['en'|'sp'|'de']: "))
                
            if t==e:
                dic2=dic.get(z),tupla[0]
                print(z,'en Español: ',tupla[0])
            elif t ==i:
                dic2=dic.get(z),tupla[1]
                print(z,'en Ingles: ',tupla[1])
            elif t ==a:
                dic2=dic.get(z),tupla[2]
                print(z,'en Aleman: ',tupla[2])
        else:
            t=str(input("Ingrese idioma ['en'|'sp'|'de']: "))
            if t==e:
                dic2=dic.get(z),tupla[0]
                print(z,'en Español: ',tupla[0])
            elif t ==i:
                dic2=dic.get(z),tupla[1]
                print(z,'en Ingles: ',tupla[1])
            elif t ==a:
                dic2=dic.get(z),tupla[2]
                print(z,'en Aleman: ',tupla[2])               
def main():
    dic={}
    agregarDicEle2(dic)
main()