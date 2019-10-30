import math
#import numpy as np
from matplotlib import pyplot as plt

#funcion lineal
#ecuacion de la recta y=m*x+b

def frecta(x,m,b):
    recta = m*x+b
    return recta

#en esta variable se mbra una lista a partir de los valores -10 y 10.
#todos estos valores seran los que tomara x

x=range(-10,10)
m=float(input("Ingrese el valor de la pendiente : "))
b=float(input("Ingrese el valor de la ordenada : "))

plt.plot(x, [frecta(i,m,b) for i in x])

for i in x:
    if i==0:
        y=frecta(0,m,b)
        plt.scatter(0,y)
        plt.text(0,y, "0,%.2f" %y, fontsize=15)
        
    if frecta(i,m,b)==0:
            plt.scatter(i,0)
            plt.text(i,0, "%.2f,0" %i, fontsize=15)
#Establecemos el color de los ejes
plt.axhline(0, color="black")
plt.axvline(0, color="black")

#Especificamos los limites del eje
plt.xlim(-20,20)
plt.ylim(-20,20)

#guardamos el grafico en una imagen "png"
plt.savefig("recta_mx+b.png")

#Colocamos la leyenda
plt.legend(['y=m*x+b',])

#mostramos el grafico
plt.ion()
plt.grid()
plt.show()