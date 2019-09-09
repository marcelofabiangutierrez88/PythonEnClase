'''
Desarrollar un programa que solicite el ingreso de un número real. Luego el
programa deberá mostrar la descomposición del número real en su parte
entera y su parte decimal, como bien muestra el ejemplo.
'''
import random
#def main():
#    nroReal = float(input("Ingrese numero: "))
#    print("Los resultados para ",nroReal," son : ")
#    parteEntera = int(nroReal)
#    parteDecimal = (nroReal)-(int(nroReal))
#    print("Parte Entera: ", parteEntera)
#    print("Parte Real: ",parteDecimal)
#main()

def desco(num):
    ent = int (num)
    dec = num-ent
    print("num=",num,"parte entera:",ent,"parte decimal:",dec)
    
def aleatorioReal():
    ent = random.randint(0,999)
    dec = (random.randint(0,99))/100
    return ent+dec
def ingresarNum():
    print ("ingrese numero:")
    x = float (input())
    return x
def main():
    num= aleatorioReal()
    desco(num)
main()