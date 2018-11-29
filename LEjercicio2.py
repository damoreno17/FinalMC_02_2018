print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------- Ejercicio 2 ----------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
#Ejercicio2
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np
import matplotlib.pylab as plt
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])

#para calcular la covarianza lo que debo hacer es:

cov(u,v):
  if len(u) !=  len(v)
  return 

   upro = np.mean(u)
   vpro= np.mean(v)
    
   suma=0
  
  for i in range (0, len(u)):
    suma += (u[i] -upro) * (v[i] - vpro)
    
  return suma/(len(u)-1)
  
    

