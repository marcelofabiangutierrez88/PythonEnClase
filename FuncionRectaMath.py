import math
import numpy as np
from matplotlib import pyplot as plt

def fRecta(x,m,x1,y1):
    y=m*x - m*x1 + y1
    return y

x = range (-10, 10)
m = float (input ("Ingrese el valor de la pendiente: "))
x1 = float (input("Ingrese el valor de la coordenada x del punto: "))
y1 = float (input("Ingrese el valor de la coordenada y le punto: "))

plt.plot(x, [fRecta(i,m,x1,y1) for i in x])

for i in x:
    if i ==0:
        y = fRecta(0,m,x1,y1)
        plt.scatter(0,y)
        plt.text(0, y, "0,%2f" %y, fontsize=15)
        
    if fRecta(i,m,x1,y1)==0:
        plt.scatter(i,0)
        plt.text(i,0,"0,%2f" %i, fontsize=15)
        
plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlim(-20,20)
plt.ylim(-20,20)

plt.savefig("recta_mx+b.png")

plt.legend(['(y-y1)=m*(x-x1)',])

plt.ion()
plt.grid()
plt.show()