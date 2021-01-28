import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generar intervalo X de las variables
#   * 
#   * 
x_sistema_refrigeracion = np.arange(0, 11, 0.1)
x_ram = np.arange(0, 11, 1)
x_procesador  = np.arange(0, 26, 1)
x_placa_madre = np.arange(0,11,1)
x_memoria_fisica = np.arange(0,11,1)
x_tarjeta_grafica = np.arange(0,11,1)
x_fuente_poder = np.arange(0,11,1)

# Generate fuzzy membership functions
sistema_refrigeracion_deficiente = fuzz.trapmf(x_sistema_refrigeracion, [0, 1,11,11])
sistema_refrigeracion_ = fuzz.trapmf(x_sistema_refrigeracion, [0, 1,11,11])


plt.plot(x_sistema_refrigeracion, qual_lo)
plt.show()

