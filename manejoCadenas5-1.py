def esLetra(texto):
    return (texto>='A' and texto<='Z') or (texto>='a' and texto<='z')

def principioFin(texto):
    pri=""
    ult=""
    pal=""
    i = 0
    while  i < len(texto):
        pal=""
        while i<len(texto) and  not esLetra(texto[i]):
            i+=1  
        while i < len(texto) and esLetra (texto[i]):
            pal = pal + texto[i]
            i+=1
      
        i+=1
        if pri =="":
            pri = pal
            ult = pal
        else: 
            ult=pal
        
    print(ult,pri)
    return ult==pri

def main():
    texto  = "hola como estas "
    principioFin(texto)
    print(principioFin(texto))
main()
            