import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generar intervalo X de las variables
#   * 
#   * 
x_sistema_refrigeracion = np.arange(0, 21, 1)
x_ram = np.arange(0, 21, 1)
x_procesador  = np.arange(0, 21, 1)
x_placa_madre = np.arange(0,21,1)
x_memoria_fisica = np.arange(0,21,1)
x_tarjeta_grafica = np.arange(0,21,1)
x_fuente_poder = np.arange(0,21,1)
x_rendimiento = np.arange(0,21,1)

# Generate fuzzy membership functions
#funcion sistema de refrigeracion
fig1, axs1 = plt.subplots(3)
sistema_refrigeracion_malo = fuzz.trapmf(x_sistema_refrigeracion, [0, 0, 2, 3])
sistema_refrigeracion_deficiente = fuzz.trapmf(x_sistema_refrigeracion, [2, 3, 5, 6])
sistema_refrigeracion_moderado = fuzz.trapmf(x_sistema_refrigeracion, [5, 6, 9, 11])
sistema_refrigeracion_bueno = fuzz.trapmf(x_sistema_refrigeracion, [7, 10, 15, 16])
sistema_refrigeracion_optimo = fuzz.trapmf(x_sistema_refrigeracion, [13, 16, 20, 20])

axs1[0].plot(x_sistema_refrigeracion, sistema_refrigeracion_malo)
axs1[0].plot(x_sistema_refrigeracion, sistema_refrigeracion_deficiente)
axs1[0].plot(x_sistema_refrigeracion, sistema_refrigeracion_moderado)
axs1[0].plot(x_sistema_refrigeracion, sistema_refrigeracion_bueno)
axs1[0].plot(x_sistema_refrigeracion, sistema_refrigeracion_optimo)

#funcion ram
ram_malo = fuzz.trapmf(x_ram, [0, 0, 2, 3])
ram_deficiente = fuzz.trapmf(x_ram, [2, 3, 5, 6])
ram_moderado = fuzz.trapmf(x_ram, [5, 6, 9, 11])
ram_bueno = fuzz.trapmf(x_ram, [7, 10, 15, 16])
ram_optimo = fuzz.trapmf(x_ram, [13, 16, 20, 20])

axs1[1].plot(x_ram, ram_malo)
axs1[1].plot(x_ram, ram_deficiente)
axs1[1].plot(x_ram, ram_moderado)
axs1[1].plot(x_ram, ram_bueno)
axs1[1].plot(x_ram, ram_optimo)

#funcion procesador
procesador_malo = fuzz.trapmf(x_procesador, [0, 0, 2, 3])
procesador_deficiente = fuzz.trapmf(x_procesador, [2, 3, 5, 6])
procesador_moderado = fuzz.trapmf(x_procesador, [5, 6, 9, 11])
procesador_bueno = fuzz.trapmf(x_procesador, [7, 10, 15, 16])
procesador_optimo = fuzz.trapmf(x_procesador, [13, 16, 20, 20])

axs1[2].plot(x_procesador, procesador_malo)
axs1[2].plot(x_procesador, procesador_deficiente)
axs1[2].plot(x_procesador, procesador_moderado)
axs1[2].plot(x_procesador, procesador_bueno)
axs1[2].plot(x_procesador, procesador_optimo)


#funcion placa madre
fig2, axs2 = plt.subplots(3)
placa_madre_malo = fuzz.trapmf(x_placa_madre, [0, 0, 2, 3])
placa_madre_deficiente = fuzz.trapmf(x_placa_madre, [2, 3, 5, 6])
placa_madre_moderado = fuzz.trapmf(x_placa_madre, [5, 6, 9, 11])
placa_madre_bueno = fuzz.trapmf(x_placa_madre, [7, 10, 15, 16])
placa_madre_optimo = fuzz.trapmf(x_placa_madre, [13, 16, 20, 20])

axs2[0].plot(x_placa_madre, placa_madre_malo)
axs2[0].plot(x_placa_madre, placa_madre_deficiente)
axs2[0].plot(x_placa_madre, placa_madre_moderado)
axs2[0].plot(x_placa_madre, placa_madre_bueno)
axs2[0].plot(x_placa_madre, placa_madre_optimo)

#funcion memoria fisica
memoria_fisica_malo = fuzz.trapmf(x_memoria_fisica, [0, 0, 2, 3])
memoria_fisica_deficiente = fuzz.trapmf(x_memoria_fisica, [2, 3, 5, 6])
memoria_fisica_moderado = fuzz.trapmf(x_memoria_fisica, [5, 6, 9, 11])
memoria_fisica_bueno = fuzz.trapmf(x_memoria_fisica, [7, 10, 15, 16])
memoria_fisica_optimo = fuzz.trapmf(x_memoria_fisica, [13, 16, 20, 20])


axs2[1].plot(x_memoria_fisica, memoria_fisica_malo)
axs2[1].plot(x_memoria_fisica, memoria_fisica_deficiente)
axs2[1].plot(x_memoria_fisica, memoria_fisica_moderado)
axs2[1].plot(x_memoria_fisica, memoria_fisica_bueno)
axs2[1].plot(x_memoria_fisica, memoria_fisica_optimo)


#funcion tarjeta grafica
tarjeta_grafica_malo = fuzz.trapmf(x_tarjeta_grafica, [0, 0, 2, 3])
tarjeta_grafica_deficiente = fuzz.trapmf(x_tarjeta_grafica, [2, 3, 5, 6])
tarjeta_grafica_moderado = fuzz.trapmf(x_tarjeta_grafica, [5, 6, 9, 11])
tarjeta_grafica_bueno = fuzz.trapmf(x_tarjeta_grafica, [7, 10, 15, 16])
tarjeta_grafica_optimo = fuzz.trapmf(x_tarjeta_grafica, [13, 16, 20, 20])

axs2[2].plot(x_tarjeta_grafica, tarjeta_grafica_malo)
axs2[2].plot(x_tarjeta_grafica, tarjeta_grafica_deficiente)
axs2[2].plot(x_tarjeta_grafica, tarjeta_grafica_moderado)
axs2[2].plot(x_tarjeta_grafica, tarjeta_grafica_bueno)
axs2[2].plot(x_tarjeta_grafica, tarjeta_grafica_optimo)

plt.figure(figsize=(10,3))

#funcion fuente oider
fuente_poder_malo = fuzz.trapmf(x_fuente_poder, [0, 0, 2, 3])
fuente_poder_deficiente = fuzz.trapmf(x_fuente_poder, [2, 3, 5, 6])
fuente_poder_moderado = fuzz.trapmf(x_fuente_poder, [5, 6, 9, 11])
fuente_poder_bueno = fuzz.trapmf(x_fuente_poder, [7, 10, 15, 16])
fuente_poder_optimo = fuzz.trapmf(x_fuente_poder, [13, 16, 20, 20])

plt.plot(x_fuente_poder, fuente_poder_malo)
plt.plot(x_fuente_poder, fuente_poder_deficiente)
plt.plot(x_fuente_poder, fuente_poder_moderado)
plt.plot(x_fuente_poder, fuente_poder_bueno)
plt.plot(x_fuente_poder, fuente_poder_optimo)

plt.figure(figsize=(10,3))

#funcion rendimiento
rendimiento_malo = fuzz.trapmf(x_rendimiento, [0, 0, 2, 3])
rendimiento_deficiente = fuzz.trapmf(x_rendimiento, [2, 3, 5, 6])
rendimiento_moderado = fuzz.trapmf(x_rendimiento, [5, 6, 9, 11])
rendimiento_bueno = fuzz.trapmf(x_rendimiento, [7, 10, 15, 16])
rendimiento_optimo = fuzz.trapmf(x_rendimiento, [13, 16, 20, 20])

plt.plot(x_rendimiento, rendimiento_malo)
plt.plot(x_rendimiento, rendimiento_deficiente)
plt.plot(x_rendimiento, rendimiento_moderado)
plt.plot(x_rendimiento, rendimiento_bueno)
plt.plot(x_rendimiento, rendimiento_optimo)

#reglas!
#Si el sistema de refrigeración y la memoria RAM y el procesador y la tarjeta de
#gráfica tienen un desempeño deficiente y la fuente de poder tiene un desempeño
#moderado
aux = np.fmin(sistema_refrigeracion_deficiente,ram_deficiente)
aux = np.fmin(aux,procesador_deficiente)
aux = np.fmin(aux,tarjeta_grafica_deficiente)
regla1 = np.fmin(aux,fuente_poder_moderado)

fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(1, 6,figsize=(18,4))
fig.suptitle('Regla 1')
ax1.plot(x_sistema_refrigeracion, sistema_refrigeracion_deficiente, color="blue")
ax1.set(xlabel="Sistema de refrigeracion")
ax2.plot(x_ram, ram_deficiente, color="orange")
ax2.set(xlabel="Ram")
ax3.plot(x_procesador, procesador_deficiente, color="red")
ax3.set(xlabel="Procesador")
ax4.plot(x_tarjeta_grafica, tarjeta_grafica_deficiente, color="green")
ax4.set(xlabel="Tarjeta gráfica")
ax5.plot(x_fuente_poder, fuente_poder_moderado, color="yellow")
ax5.set(xlabel="Fuente de poder")

ax6.plot(x_rendimiento, rendimiento_deficiente, color="pink")
ax6.set(xlabel="Rendimiento")
plt.savefig('Regla 1.png')


plt.show()

