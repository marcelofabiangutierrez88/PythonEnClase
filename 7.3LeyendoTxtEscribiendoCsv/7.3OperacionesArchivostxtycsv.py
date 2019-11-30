import csv

def leerArchivos():
 with open("ejercicio.txt","r") as archivo:
    for linea in archivo:
    
        listaPalabras=linea.split()
        frecuenciaPal=[]
        for w in listaPalabras:
            frecuenciaPal.append(listaPalabras.count(w))
        print(str(listaPalabras))
        frecuenciaAsig= dict(zip(listaPalabras,frecuenciaPal))
        
 with open('resultado.csv','a') as f:
        w = csv.writer(f)
        w.writerows(frecuenciaAsig.items())
        print("Escribiendo diccionario en resultado.csv...")
        
def main():
    leerArchivos()
main()