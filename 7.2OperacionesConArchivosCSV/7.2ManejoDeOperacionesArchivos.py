import csv
def leerArchivos():

    with open('ejercicio.csv') as File:
        arch=open('ejercicio.csv')
        reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
        for col in reader:
            colInt=[int (col[0]), int (col[1]), int (col[2]),int (col[3]),int (col[4]),int (col[5])]               
            colFi=[]
            colFi = [colInt]
            print("Columna convertida en listas",(colFi))
            suma=sum(colFi[0])
            prome=""
            prom=suma/len(colFi[0])
            print("Promedio Fila: ",prom,"\n")
            
#             with open('resultado.csv','a') as file:
#                 w = csv.writer(file)
#                 w.writerows(prom)
#                 print("Escribiendo en resultado.csv...")
            
    arch.close()
def main():
    leerArchivos()
main()