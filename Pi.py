from random import random
from math import hypot
from matplotlib import pyplot as plt
import sys
from PIL import Image
from PIL import ImageDraw

print (' ')
print ('Cuantos numeros aleatorios? ')
NumPuntos=int(input('NumPuntos:'))

Ncirculo=0
for i in range (NumPuntos):
  x=random()
  y=random()
  if hypot(x,y)<1:
    Ncirculo=Ncirculo+1
    plt.plot(x,y,'ro')
plt.savefig('CuartoDeCirculo.png')
plt.show()
print (' ')
print ('pi= '+str(4.0*Ncirculo/NumPuntos))
print (' ')

