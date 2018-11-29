print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------- Ejercicio 4 ----------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")

# Ejercicio4
# Tiene una serie de tiempo, donde los datos de tiempo estan almacenados en un arreglo t y los datos de amplitud en un arreglo amp.
#1) Usando los paquetes de scipy de la transformada de Fourier, haga un FILTRO de la senial que elimine las frecuencias mayores a 1000Hz en las senial original.
#2) Haga una grafica de la senial original y la senial filtarada y guardela SIN MOSTRARLA en filtro.pdf
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft

n = 1280 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 320 ) #El paso, 320 samples per unit frequency
t = np.linspace( 0, (n-1)*dt, n)
amp = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t ) + np.random.random(n)

# SU FILTRO
func (t, amp):
  for amp in func
    if amp > 1000 or amp < -1000
      remove amp
     else
      amp2= amp
      
print (amp)

# SU GRAFICA
plt.plot (t,amp)
plt.ṕlot(t,amp2)
plt.show()

# Puede usar los siguientes paquetes:


