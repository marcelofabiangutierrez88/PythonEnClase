import pandas as pd
import csv

def leerArchivo():
    datos=pd.read_csv('Personas.csv',header=0)
    df=pd.DataFrame(datos)
    print(datos,"\n")
    return df

def escribirArchivo():
    with open('Personas.csv', 'a') as csvfile:
        fieldnames = ['NOMBRE', 'APELLIDO', 'DNI']
        print("Ingrese los datos que se le solicitan para generar un nuevo registro \n")
        nombre=input("Ingrese nombre: ")
        ape=input("Ingrese Apellido: ")
        dni=int(input("Ingrese DNI: "))
        #falta validacion del dni repetido.
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows([{'NOMBRE': nombre, 'APELLIDO': ape, 'DNI': dni}])
        print("Escritura completa....")
    csvfile.close()

def buscar(df):
    opcion=int(input("Ingrese 1 para buscar por apellido o 2 para buscar por DNI o 0 para salir: \n"))
    while opcion != 0:
        if opcion==1:
            ape = input("Introduce apellido :")
            buscador = df[df['APELLIDO'] == ape]
            print (buscador)
        else:
            dni= int(input("Introduce DNI: "))
            buscador = df[df['DNI']==dni]
            print(buscador)
        break
  
def eliminar(df):
    borrar=int(input("Ingrese DNI del registro a borrar: "))
    borrado = df.drop(df[df['DNI']==borrar].index,axis=0,inplace=True)
    print("Se ha eliminado el registro: ",borrar,borrado,"\n")
    

def ordenar(df):
    opcion=int(input("Ingrese 1 para ordenar por NOMBRE, 2 para ordenar por APELLIDO, 3 para ordenar por DNI: "))
    if opcion ==1:
        nombre = df.sort_values(by=['NOMBRE'],ascending =[True])
        print(nombre)
    elif opcion ==2:
        ape=df.sort_values(by=['APELLIDO'], ascending = [True])
        print(ape)
    elif opcion ==3:
        dni = df.sort_values(by=['DNI'], ascending=[True])
        print(dni)
    
def main():
    datos=pd.read_csv('Personas.csv',header=0)
    df=pd.DataFrame(datos)
    opcion=0
    while opcion!=6:
        print("1. AGREGAR REGISTRO:")
        print("2. ELIMINAR REGISTRO: ")
        print("3. BUSCAR REGISTRO: ")
        print("4. ORDENAR ARCHIVO POR : ")
        print("5. MOSTRAR ARCHIVO ")
        print("6. SALIR")
        opcion = int (input("ingrese la opcion deseada: "))
        if opcion == 1:
            escribirArchivo()
            print()
        if opcion ==2 :
            eliminar(df)
            print()
        if opcion ==3:
            buscar(df)
            print()
        if opcion ==4:
            ordenar(df)
            print()
        if opcion ==5:
            leerArchivo()
            print()
        if opcion ==6:
            print("Gracias... Hasta Luego.")
main()

