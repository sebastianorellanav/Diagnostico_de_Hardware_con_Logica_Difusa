import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt 
import fuzzyfunctions as ff 
def areaZero (areas):
	total = 0
	for area in areas:
		total += area
	if total == 0:
		return True
	return False
def maxAndPos(candidates):
	i = 0
	position = 0
	valor = candidates[0]
	while i < len(candidates):
		if valor < candidates[i]:
			valor = candidates[i]
			position = i
		i += 1
	return valor, position
def interpretateRendimiento(position):
	if position == 0:
		return "Rendimiento de grado malo"
	elif (position == 1):
		return "Rendimiento de grado deficiente"
	elif(position == 2):
		return "Rendimiento de grado Moderado"
	elif(position == 3):
		return "Rendimiento de grado Bueno"
	elif(position == 4):
		return "Rendimiento de grado Optimo"
		   


def fuzzy_model(sistema_refrigeracion_in, ram_in, procesador_in, placa_madre_in, memoria_fisica_in, tarjeta_grafica_in, fuente_poder_in):
	########## INPUTS ########################
	#Input Universe functions

	x_sistema_refrigeracion = np.arange(0, 11, 1)
	x_ram =  np.arange(0, 11, 1)
	x_procesador  = np.arange(0, 11, 1)
	x_placa_madre = np.arange(0, 11, 1)
	x_memoria_fisica = np.arange(0, 11, 1)
	x_tarjeta_grafica = np.arange(0, 11, 1)
	x_fuente_poder = np.arange(0, 11, 1)
	x_rendimiento = np.arange(0, 11, 1)

	# Input Membership Functions
	# sistema de refrigeracion
	sistema_refrigeracion_malo = fuzz.trimf(x_sistema_refrigeracion, [0,0,2])
	sistema_refrigeracion_deficiente = fuzz.trimf(x_sistema_refrigeracion, [0,2,4])
	sistema_refrigeracion_moderado = fuzz.trimf(x_sistema_refrigeracion, [2,4,6])
	sistema_refrigeracion_bueno = fuzz.trimf(x_sistema_refrigeracion, [4,6,8])
	sistema_refrigeracion_optimo = fuzz.trapmf(x_sistema_refrigeracion, [6,8,10,10])


	# ram
	ram_malo = fuzz.trimf(x_ram, [0,0,2])
	ram_deficiente = fuzz.trimf(x_ram, [0,2,4])
	ram_moderado = fuzz.trimf(x_ram, [2,4,6])
	ram_bueno = fuzz.trimf(x_ram, [4,6,8])
	ram_optimo = fuzz.trapmf(x_ram, [6,8,10,10])

	# procesador
	procesador_malo = fuzz.trimf(x_procesador, [0,0,2])
	procesador_deficiente = fuzz.trimf(x_procesador, [0,2,4])
	procesador_moderado = fuzz.trimf(x_procesador, [2,4,6])
	procesador_bueno = fuzz.trimf(x_procesador, [4,6,8])
	procesador_optimo = fuzz.trapmf(x_procesador, [6,8,10,10])

	# placa madre
	placa_madre_malo = fuzz.trimf(x_placa_madre, [0,0,2])
	placa_madre_deficiente = fuzz.trimf(x_placa_madre, [0,2,4])
	placa_madre_moderado = fuzz.trimf(x_placa_madre, [2,4,6])
	placa_madre_bueno = fuzz.trimf(x_placa_madre, [4,6,8])
	placa_madre_optimo = fuzz.trapmf(x_placa_madre, [6,8,10,10])

# memoria fisica
	memoria_fisica_malo = fuzz.trimf(x_memoria_fisica, [0,0,2])
	memoria_fisica_deficiente = fuzz.trimf(x_memoria_fisica, [0,2,4])
	memoria_fisica_moderado = fuzz.trimf(x_memoria_fisica, [2,4,6])
	memoria_fisica_bueno = fuzz.trimf(x_memoria_fisica, [4,6,8])
	memoria_fisica_optimo = fuzz.trapmf(x_memoria_fisica, [6,8,10,10])

	# tarjeta grafica
	tarjeta_grafica_malo = fuzz.trimf(x_tarjeta_grafica, [0,0,2])
	tarjeta_grafica_deficiente = fuzz.trimf(x_tarjeta_grafica, [0,2,4])
	tarjeta_grafica_moderado = fuzz.trimf(x_tarjeta_grafica, [2,4,6])
	tarjeta_grafica_bueno = fuzz.trimf(x_tarjeta_grafica, [4,6,8])
	tarjeta_grafica_optimo = fuzz.trapmf(x_tarjeta_grafica, [6,8,10,10])

	# fuente poder
	fuente_poder_malo = fuzz.trimf(x_fuente_poder, [0,0,2])
	fuente_poder_deficiente = fuzz.trimf(x_fuente_poder, [0,2,4])
	fuente_poder_moderado = fuzz.trimf(x_fuente_poder, [2,4,6])
	fuente_poder_bueno = fuzz.trimf(x_fuente_poder, [4,6,8])
	fuente_poder_optimo = fuzz.trapmf(x_fuente_poder, [6,8,10,10])


	# rendimiento_COA
	rendimiento_malo = fuzz.trimf(x_rendimiento, [0,0,2])
	rendimiento_deficiente = fuzz.trimf(x_rendimiento, [0,2,4])
	rendimiento_moderado = fuzz.trimf(x_rendimiento, [2,4,6])
	rendimiento_bueno = fuzz.trimf(x_rendimiento, [4,6,8])
	rendimiento_optimo = fuzz.trapmf(x_rendimiento, [6,8,10,10])


	fig0, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

	ax0.plot(x_sistema_refrigeracion, sistema_refrigeracion_malo, 'b', linewidth=1.5, label='Malo')
	ax0.plot(x_sistema_refrigeracion, sistema_refrigeracion_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax0.plot(x_sistema_refrigeracion, sistema_refrigeracion_moderado, 'r', linewidth=1.5, label='Moderado')
	ax0.plot(x_sistema_refrigeracion, sistema_refrigeracion_bueno, c = 'darkorange', linewidth=1.5, label='Bueno')
	ax0.plot(x_sistema_refrigeracion, sistema_refrigeracion_optimo, c = 'magenta', linewidth=1.5, label='Optimo')

	ax0.set_title('Sistema de refrigeracion')
	ax0.legend()

	ax1.plot(x_ram, ram_malo, 'b', linewidth=1.5, label='Malo')
	ax1.plot(x_ram, ram_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax1.plot(x_ram, ram_moderado, 'r', linewidth=1.5, label='Moderado')
	ax1.plot(x_ram, ram_bueno, c = 'darkorange', linewidth=1.5, label='Bueno')
	ax1.plot(x_ram, ram_optimo, c = 'magenta', linewidth=1.5, label='Optimo')

	ax1.set_title('Ram')
	ax1.legend()

	ax2.plot(x_procesador, procesador_malo, 'b', linewidth=1.5, label='Malo')
	ax2.plot(x_procesador, procesador_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax2.plot(x_procesador, procesador_moderado, 'r', linewidth=1.5, label='Moderado')
	ax2.plot(x_procesador, procesador_bueno, c = 'darkorange', linewidth=1.5, label='Bueno')
	ax2.plot(x_procesador, procesador_optimo, c = 'magenta', linewidth=1.5, label='Optimo')

	ax2.set_title('Procesador')
	ax2.legend()



	# Turn off top/right axes
	for ax in (ax0, ax1, ax2):
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)
		ax.get_xaxis().tick_bottom()
		ax.get_yaxis().tick_left()

	fig1, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8, 12))

	ax0.plot(x_placa_madre, placa_madre_malo, 'b', linewidth=1.5, label='Malo')
	ax0.plot(x_placa_madre, placa_madre_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax0.plot(x_placa_madre, placa_madre_moderado, 'r', linewidth=1.5, label='Moderado')
	ax0.plot(x_placa_madre, placa_madre_bueno, c = 'darkorange', linewidth=1.5, label='Bueno')
	ax0.plot(x_placa_madre, placa_madre_optimo, c = 'magenta', linewidth=1.5, label='Optimo')

	ax0.set_title('Placa madre')
	ax0.legend()

	ax1.plot(x_memoria_fisica, memoria_fisica_malo, 'b', linewidth=1.5, label='Malo')
	ax1.plot(x_memoria_fisica, memoria_fisica_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax1.plot(x_memoria_fisica, memoria_fisica_moderado, 'r', linewidth=1.5, label='Moderado')
	ax1.plot(x_memoria_fisica, memoria_fisica_bueno, c = 'darkorange', linewidth=1.5, label='Bueno')
	ax1.plot(x_memoria_fisica, memoria_fisica_optimo, c = 'magenta', linewidth=1.5, label='Optimo')

	ax1.set_title('Memoria física')
	ax1.legend()

	ax2.plot(x_tarjeta_grafica, tarjeta_grafica_malo, 'b', linewidth=1.5, label='Malo')
	ax2.plot(x_tarjeta_grafica, tarjeta_grafica_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax2.plot(x_tarjeta_grafica, tarjeta_grafica_moderado, 'r', linewidth=1.5, label='Moderado')
	ax2.plot(x_tarjeta_grafica, tarjeta_grafica_bueno, c = 'darkorange', linewidth=1.5, label='Bueno')
	ax2.plot(x_tarjeta_grafica, tarjeta_grafica_optimo, c = 'magenta', linewidth=1.5, label='Optimo')

	ax2.set_title('Tarjeta gráfica')
	ax2.legend()

	ax3.plot(x_fuente_poder, fuente_poder_malo, 'b', linewidth=1.5, label='Malo')
	ax3.plot(x_fuente_poder, fuente_poder_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax3.plot(x_fuente_poder, fuente_poder_moderado, 'r', linewidth=1.5, label='Moderado')
	ax3.plot(x_fuente_poder, fuente_poder_bueno, c = 'darkorange', linewidth=1.5, label='Bueno')
	ax3.plot(x_fuente_poder, fuente_poder_optimo, c = 'magenta', linewidth=1.5, label='Optimo')

	ax3.set_title('Fuente de poder')
	ax3.legend()




	# Turn off top/right axes
	for ax in (ax0, ax1, ax2):
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)
		ax.get_xaxis().tick_bottom()
		ax.get_yaxis().tick_left()  




	regla1=np.fmin(sistema_refrigeracion_deficiente[sistema_refrigeracion_in],
			np.fmin(ram_deficiente[ram_in],
				np.fmin(procesador_deficiente[procesador_in],
					np.fmin(tarjeta_grafica_deficiente[tarjeta_grafica_in],fuente_poder_moderado[fuente_poder_in])
					)
				)
			)
	regla2=np.fmin(procesador_moderado[procesador_in],
			np.fmin(sistema_refrigeracion_malo[sistema_refrigeracion_in],
				np.fmin(ram_moderado[ram_in],
					np.fmin(placa_madre_bueno[placa_madre_in],
						np.fmin(tarjeta_grafica_malo[tarjeta_grafica_in],fuente_poder_bueno[fuente_poder_in])
						)
					)
				)
			)
	regla3=np.fmin(placa_madre_optimo[placa_madre_in],
			np.fmin(procesador_optimo[procesador_in],
				np.fmin(ram_moderado[ram_in],fuente_poder_moderado[fuente_poder_in]
					)
				)
			)
	regla4=np.fmax(fuente_poder_moderado[fuente_poder_in],
			np.fmax(memoria_fisica_bueno[memoria_fisica_in],
				np.fmax(placa_madre_moderado[placa_madre_in],sistema_refrigeracion_optimo[sistema_refrigeracion_in]
					)
				)
			)
	regla5=np.fmin(ram_optimo[ram_in],placa_madre_optimo[placa_madre_in])

	regla6 = np.fmin(np.fmax(placa_madre_deficiente[placa_madre_in],
						sistema_refrigeracion_moderado[sistema_refrigeracion_in]),
						np.fmax(procesador_bueno[procesador_in],
						ram_bueno[ram_in]))

	regla7 = np.fmin(sistema_refrigeracion_optimo[sistema_refrigeracion_in],
						np.fmin(ram_moderado[ram_in], 
						np.fmin(procesador_moderado[procesador_in],
						np.fmin(tarjeta_grafica_moderado[tarjeta_grafica_in], 
						placa_madre_bueno[placa_madre_in]))))


	imp1= np.fmin(regla1,rendimiento_deficiente)
	imp2= np.fmin(regla2,rendimiento_bueno)
	imp3= np.fmin(regla3,rendimiento_bueno)
	imp4= np.fmin(regla4,rendimiento_moderado)
	imp5= np.fmin(regla5,rendimiento_optimo)
	imp6= np.fmin(regla6,rendimiento_malo)
	imp7= np.fmin(regla7,rendimiento_moderado)

	rendimiento0 = np.zeros_like(x_rendimiento)

	fig3, ax0 = plt.subplots(figsize=(8, 3))

	ax0.fill_between(x_rendimiento, rendimiento0, imp1, facecolor='b', alpha=0.7)
	ax0.plot(x_rendimiento, rendimiento_deficiente, 'b', linewidth=0.5, linestyle='--', )
	ax0.fill_between(x_rendimiento, rendimiento0, imp2, facecolor='g', alpha=0.7)
	ax0.plot(x_rendimiento, rendimiento_bueno, 'g', linewidth=0.5, linestyle='--')
	ax0.fill_between(x_rendimiento, rendimiento0, imp3, facecolor='r', alpha=0.7)
	ax0.plot(x_rendimiento, rendimiento_bueno, 'r', linewidth=0.5, linestyle='--')
	ax0.fill_between(x_rendimiento, rendimiento0, imp4, facecolor='c', alpha=0.7)
	ax0.plot(x_rendimiento, rendimiento_moderado, 'c', linewidth=0.5, linestyle='--')
	ax0.fill_between(x_rendimiento, rendimiento0, imp5, facecolor='m', alpha=0.7)
	ax0.plot(x_rendimiento, rendimiento_optimo, 'm', linewidth=0.5, linestyle='--')
	ax0.fill_between(x_rendimiento, rendimiento0, imp6, facecolor='k', alpha=0.7)
	ax0.plot(x_rendimiento, rendimiento_malo, 'k', linewidth=0.5, linestyle='--')
	ax0.fill_between(x_rendimiento, rendimiento0, imp7, facecolor='y', alpha=0.7)
	ax0.plot(x_rendimiento, rendimiento_moderado, 'k', linewidth=0.5, linestyle='--')

	ax0.set_title('Nivel de rendimiento_COA')

	# Turn off top/right axes
	for ax in (ax0,):
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)
		ax.get_xaxis().tick_bottom()
		ax.get_yaxis().tick_left()


	#Step 5: Aggregate all output - max
	aggregate_membership = np.fmax(imp1, np.fmax(imp2, np.fmax(imp3, np.fmax(imp4,
									np.fmax(imp5, np.fmax(imp6, imp7))))))

	#Step 6: Defuzzify using Centroid
	try:
		resultado_COA = fuzz.defuzz(x_rendimiento, aggregate_membership , 'centroid')
	except:
		resultado_COA = 0

	print(resultado_COA)
	try:
		resultado_BOA = fuzz.defuzz(x_rendimiento, aggregate_membership , 'bisector')
	except:
		resultado_BOA = 0


	if areaZero(aggregate_membership):
		print("\n----->> Error <<-----\n")  # Aqui se puede cambiar por otro mensaje.
											# Opciones:
											#           * "El área es 0 y por ende indicar que no tiene rendimiento_COA"
											#           * "El área es 0, indicar error de opereaciones, en base a valores ingresados"
	else:
		# Se calcula el centroide para desfuzificar (COA)
		rendimiento_COA = fuzz.defuzz(x_rendimiento, aggregate_membership, 'centroide')
		rendimiento_plot = fuzz.interp_membership(x_rendimiento, aggregate_membership, rendimiento_COA)  # for plot

		# Se visualiza el grafico
		fig, ax0 = plt.subplots(figsize=(8, 3))

		ax0.plot(x_rendimiento, rendimiento_malo, 'b', linewidth=0.5, linestyle='--')
		ax0.plot(x_rendimiento, rendimiento_deficiente, 'g', linewidth=0.5, linestyle='--')
		ax0.plot(x_rendimiento, rendimiento_moderado, 'r', linewidth=0.5, linestyle='--')
		ax0.plot(x_rendimiento, rendimiento_bueno, 'm', linewidth=0.5, linestyle='--')
		ax0.plot(x_rendimiento, rendimiento_optimo, c='darkorange', linewidth=0.5, linestyle='--')
		ax0.fill_between(x_rendimiento, rendimiento0, aggregate_membership, facecolor='Orange', alpha=0.7)
		ax0.plot([rendimiento_COA, rendimiento_COA], [0, rendimiento_plot], 'k', linewidth=1.5, alpha=0.9)
		ax0.set_title('Resultado al desfuzificar')

		# Turn off top/right axes
		for ax in (ax0,):
			ax.spines['top'].set_visible(False)
			ax.spines['right'].set_visible(False)
			ax.get_xaxis().tick_bottom()
			ax.get_yaxis().tick_left()

		plt.ion()
		plt.show()


		rendimiento_resultLow = fuzz.interp_membership(x_rendimiento, rendimiento_malo, rendimiento_COA)
		rendimiento_resultMD = fuzz.interp_membership(x_rendimiento, rendimiento_deficiente, rendimiento_COA)
		rendimiento_resultH = fuzz.interp_membership(x_rendimiento, rendimiento_moderado, rendimiento_COA)
		rendimiento_resultVH = fuzz.interp_membership(x_rendimiento, rendimiento_bueno, rendimiento_COA)
		rendimiento_resultO = fuzz.interp_membership(x_rendimiento, rendimiento_optimo, rendimiento_COA)


		belognsTo, resultPosition = maxAndPos([rendimiento_resultLow, rendimiento_resultMD, rendimiento_resultH, rendimiento_resultVH,rendimiento_resultO])
		rendimiento_estimacion = interpretateRendimiento(resultPosition)

		print("En base a los datos ingresados, y al 'valor de pertenencia' obtenido (",belognsTo,").\nEs que se estima que padece",rendimiento_estimacion)




	print(resultado_BOA)
	return [0,0]
