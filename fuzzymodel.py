import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt 

# Función que verifica si el area bajo la curva es cero
# Entrada: lista
# Salida:  booleano
def areaZero (areas):
	total = 0
	for area in areas:
		total += area
	if total == 0:
		return True
	return False

# Función que busca el máximo valor y su posición en la lista
# Entrada: lista
# Salida:  entero (valor)
#          entero (posición)
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

# Función que interpreta el resultado de la desfucificación
# Entrada: entero
# Salida:  string
def interpretateRendimiento(position):
	if position == 0:
		return "Malo"
	elif (position == 1):
		return "Deficiente"
	elif(position == 2):
		return "Moderado"
	elif(position == 3):
		return "Bueno"
	elif(position == 4):
		return "Optimo"
		   
# Función que simula el modelo de lógica difusa
# Entrada: entero (input sistema de refrigeracion)
#          entero (input ram)
#          entero (input procesador)
#		   entero (input placa madre)
#		   entero (input memoria física)
#		   entero (input tarjeta gráfica)
#		   entero (input fuente de poder)
# Salida:  lista (resultado de la desfucificación)
def fuzzy_model(sistema_refrigeracion_in, ram_in, procesador_in, placa_madre_in, memoria_fisica_in, tarjeta_grafica_in, fuente_poder_in):

	# Vectores x de cada una de las funciones de pertenencia
	x_sistema_refrigeracion = np.arange(0, 11, 1)
	x_ram =  np.arange(0, 11, 1)
	x_procesador  = np.arange(0, 11, 1)
	x_placa_madre = np.arange(0, 11, 1)
	x_memoria_fisica = np.arange(0, 11, 1)
	x_tarjeta_grafica = np.arange(0, 11, 1)
	x_fuente_poder = np.arange(0, 11, 1)
	x_rendimiento = np.arange(0, 11, 1)

	# Funciones de Pertenencia
	# sistema de refrigeracion
	sistema_refrigeracion_malo = fuzz.trapmf(x_sistema_refrigeracion, [0,0,1,4])
	sistema_refrigeracion_deficiente = fuzz.trimf(x_sistema_refrigeracion, [0,3,6])
	sistema_refrigeracion_moderado = fuzz.trimf(x_sistema_refrigeracion, [2,5,8])
	sistema_refrigeracion_bueno = fuzz.trimf(x_sistema_refrigeracion, [4,7,10])
	sistema_refrigeracion_optimo = fuzz.trapmf(x_sistema_refrigeracion, [6,9,12,12])

	# ram
	ram_malo = fuzz.trapmf(x_ram, [0,0,1,4])
	ram_deficiente = fuzz.trimf(x_ram, [0,3,6])
	ram_moderado = fuzz.trimf(x_ram, [2,5,8])
	ram_bueno = fuzz.trimf(x_ram, [4,7,10])
	ram_optimo = fuzz.trapmf(x_ram, [6,9,12,12])

	# procesador
	procesador_malo = fuzz.trapmf(x_procesador, [0,0,1,4])
	procesador_deficiente = fuzz.trimf(x_procesador, [0,3,6])
	procesador_moderado = fuzz.trimf(x_procesador, [2,5,8])
	procesador_bueno = fuzz.trimf(x_procesador, [4,7,10])
	procesador_optimo = fuzz.trapmf(x_procesador, [6,9,12,12])

	# placa madre
	placa_madre_malo = fuzz.trapmf(x_placa_madre, [0,0,1,4])
	placa_madre_deficiente = fuzz.trimf(x_placa_madre, [0,3,6])
	placa_madre_moderado = fuzz.trimf(x_placa_madre, [2,5,8])
	placa_madre_bueno = fuzz.trimf(x_placa_madre, [4,7,10])
	placa_madre_optimo = fuzz.trapmf(x_placa_madre, [6,9,12,12])

	# memoria fisica
	memoria_fisica_malo = fuzz.trapmf(x_memoria_fisica, [0,0,1,4])
	memoria_fisica_deficiente = fuzz.trimf(x_memoria_fisica, [0,3,6])
	memoria_fisica_moderado = fuzz.trimf(x_memoria_fisica, [2,5,8])
	memoria_fisica_bueno = fuzz.trimf(x_memoria_fisica, [4,7,10])
	memoria_fisica_optimo = fuzz.trapmf(x_memoria_fisica, [6,9,12,12])

	# tarjeta grafica
	tarjeta_grafica_malo = fuzz.trapmf(x_tarjeta_grafica, [0,0,1,4])
	tarjeta_grafica_deficiente = fuzz.trimf(x_tarjeta_grafica, [0,3,6])
	tarjeta_grafica_moderado = fuzz.trimf(x_tarjeta_grafica, [2,5,8])
	tarjeta_grafica_bueno = fuzz.trimf(x_tarjeta_grafica, [4,7,10])
	tarjeta_grafica_optimo = fuzz.trapmf(x_tarjeta_grafica, [6,9,12,12])

	# fuente poder
	fuente_poder_malo = fuzz.trapmf(x_fuente_poder, [0,0,1,4])
	fuente_poder_deficiente = fuzz.trimf(x_fuente_poder, [0,3,6])
	fuente_poder_moderado = fuzz.trimf(x_fuente_poder, [2,5,8])
	fuente_poder_bueno = fuzz.trimf(x_fuente_poder, [4,7,10])
	fuente_poder_optimo = fuzz.trapmf(x_fuente_poder, [6,9,12,12])

	# Consecuente
	# rendimiento
	rendimiento_malo = fuzz.trapmf(x_rendimiento, [0,0,1,4])
	rendimiento_deficiente = fuzz.trimf(x_rendimiento, [0,3,6])
	rendimiento_moderado = fuzz.trimf(x_rendimiento, [2,5,8])
	rendimiento_bueno = fuzz.trimf(x_rendimiento, [4,7,10])
	rendimiento_optimo = fuzz.trapmf(x_rendimiento, [6,9,12,12])

	###################################################################################################################################
	# Se grafican las funciones de pertenencia
	fig0, (ax0, ax1) = plt.subplots(nrows=2, figsize=(8, 12))

	ax0.plot(x_sistema_refrigeracion, sistema_refrigeracion_malo, 'b', linewidth=1.5, label='Malo')
	ax0.plot(x_sistema_refrigeracion, sistema_refrigeracion_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax0.plot(x_sistema_refrigeracion, sistema_refrigeracion_moderado, 'r', linewidth=1.5, label='Moderado')
	ax0.plot(x_sistema_refrigeracion, sistema_refrigeracion_bueno, c = 'darkorange', linewidth=1.5, label='Bueno')
	ax0.plot(x_sistema_refrigeracion, sistema_refrigeracion_optimo, c = 'magenta', linewidth=1.5, label='Optimo')
	ax0.set_title('Sistema de refrigeracion')

	ax0.legend()

	ax1.plot(x_ram, ram_malo, 'b', linewidth=1.5, label='Mala')
	ax1.plot(x_ram, ram_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax1.plot(x_ram, ram_moderado, 'r', linewidth=1.5, label='Moderada')
	ax1.plot(x_ram, ram_bueno, c = 'darkorange', linewidth=1.5, label='Buena')
	ax1.plot(x_ram, ram_optimo, c = 'magenta', linewidth=1.5, label='Optima')
	ax1.set_title('Ram')
	ax1.legend()

	# Se hacen invisibles las lineas de arriba y la derecha

	for ax in (ax0, ax1):
		ax.set_ylabel("Grado de pertenencia")
		ax.set_xlabel("Grado de funcionalidad (Puntuación)")
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)
		ax.get_xaxis().tick_bottom()
		ax.get_yaxis().tick_left()
	
	fig1, (ax0, ax1) = plt.subplots(nrows=2, figsize=(8, 12))

	ax0.plot(x_procesador, procesador_malo, 'b', linewidth=1.5, label='Malo')
	ax0.plot(x_procesador, procesador_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax0.plot(x_procesador, procesador_moderado, 'r', linewidth=1.5, label='Moderado')
	ax0.plot(x_procesador, procesador_bueno, c = 'darkorange', linewidth=1.5, label='Bueno')
	ax0.plot(x_procesador, procesador_optimo, c = 'magenta', linewidth=1.5, label='Optimo')
	ax0.set_title('Procesador')
	ax0.legend()

	ax1.plot(x_placa_madre, placa_madre_malo, 'b', linewidth=1.5, label='Mala')
	ax1.plot(x_placa_madre, placa_madre_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax1.plot(x_placa_madre, placa_madre_moderado, 'r', linewidth=1.5, label='Moderada')
	ax1.plot(x_placa_madre, placa_madre_bueno, c = 'darkorange', linewidth=1.5, label='Buena')
	ax1.plot(x_placa_madre, placa_madre_optimo, c = 'magenta', linewidth=1.5, label='Optima')
	ax1.set_title('Placa madre')
	ax1.legend()

	# Se hacen invisibles las lineas de arriba y la derecha

	for ax in (ax0, ax1):
		ax.set_ylabel("Grado de pertenencia")
		ax.set_xlabel("Grado de funcionalidad (Puntuación)")
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)
		ax.get_xaxis().tick_bottom()
		ax.get_yaxis().tick_left()

	fig2, (ax1, ax2, ax3) = plt.subplots(nrows=3, figsize=(8, 12))
	plt.subplots_adjust(hspace= 0.4)

	ax1.plot(x_memoria_fisica, memoria_fisica_malo, 'b', linewidth=1.5, label='Mala')
	ax1.plot(x_memoria_fisica, memoria_fisica_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax1.plot(x_memoria_fisica, memoria_fisica_moderado, 'r', linewidth=1.5, label='Moderada')
	ax1.plot(x_memoria_fisica, memoria_fisica_bueno, c = 'darkorange', linewidth=1.5, label='Buena')
	ax1.plot(x_memoria_fisica, memoria_fisica_optimo, c = 'magenta', linewidth=1.5, label='Optima')
	ax1.set_title('Memoria física')
	ax1.legend()

	ax2.plot(x_tarjeta_grafica, tarjeta_grafica_malo, 'b', linewidth=1.5, label='Mala')
	ax2.plot(x_tarjeta_grafica, tarjeta_grafica_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax2.plot(x_tarjeta_grafica, tarjeta_grafica_moderado, 'r', linewidth=1.5, label='Moderada')
	ax2.plot(x_tarjeta_grafica, tarjeta_grafica_bueno, c = 'darkorange', linewidth=1.5, label='Buena')
	ax2.plot(x_tarjeta_grafica, tarjeta_grafica_optimo, c = 'magenta', linewidth=1.5, label='Optima')
	ax2.set_title('Tarjeta gráfica')
	ax2.legend()

	ax3.plot(x_fuente_poder, fuente_poder_malo, 'b', linewidth=1.5, label='Mala')
	ax3.plot(x_fuente_poder, fuente_poder_deficiente, 'g', linewidth=1.5, label='Deficiente')
	ax3.plot(x_fuente_poder, fuente_poder_moderado, 'r', linewidth=1.5, label='Moderada')
	ax3.plot(x_fuente_poder, fuente_poder_bueno, c = 'darkorange', linewidth=1.5, label='Buena')
	ax3.plot(x_fuente_poder, fuente_poder_optimo, c = 'magenta', linewidth=1.5, label='Optima')
	ax3.set_title('Fuente de poder')
	ax3.legend()

	# Se hacen invisibles las lineas de arriba y la derecha

	for ax in (ax1, ax2, ax3):
		ax.set_ylabel("Grado de pertenencia")
		ax.set_xlabel("Grado de funcionalidad (Puntuación)")
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)
		ax.get_xaxis().tick_bottom()
		ax.get_yaxis().tick_left()
	
	##############################################################################################################################
	# Reglas

	# Regla 1
	regla1 =np.fmin(sistema_refrigeracion_deficiente[sistema_refrigeracion_in],
			np.fmin(ram_deficiente[ram_in],
			np.fmin(procesador_deficiente[procesador_in],
			np.fmin(tarjeta_grafica_deficiente[tarjeta_grafica_in],fuente_poder_moderado[fuente_poder_in]))))
	
	# Regla 2
	regla2 =np.fmin(procesador_moderado[procesador_in],
			np.fmin(sistema_refrigeracion_malo[sistema_refrigeracion_in],
			np.fmin(ram_moderado[ram_in],
			np.fmin(placa_madre_bueno[placa_madre_in],
			np.fmin(tarjeta_grafica_malo[tarjeta_grafica_in],fuente_poder_bueno[fuente_poder_in])))))

	# Regla 3
	regla3 =np.fmin(placa_madre_optimo[placa_madre_in],
			np.fmin(procesador_optimo[procesador_in],
			np.fmin(ram_moderado[ram_in],fuente_poder_moderado[fuente_poder_in])))

	# Regla 4
	regla4 =np.fmax(fuente_poder_moderado[fuente_poder_in],
			np.fmax(memoria_fisica_bueno[memoria_fisica_in],
			np.fmax(placa_madre_moderado[placa_madre_in],sistema_refrigeracion_bueno[sistema_refrigeracion_in])))

	# Regla 5
	regla5 =np.fmin(ram_optimo[ram_in],placa_madre_optimo[placa_madre_in])

	# Regla 6
	regla6 =np.fmin(np.fmax(placa_madre_deficiente[placa_madre_in],
			sistema_refrigeracion_moderado[sistema_refrigeracion_in]),
			np.fmax(procesador_bueno[procesador_in],
			ram_bueno[ram_in]))

	# Regla 7
	regla7 =np.fmin(sistema_refrigeracion_optimo[sistema_refrigeracion_in],
			np.fmin(ram_moderado[ram_in], 
			np.fmin(procesador_moderado[procesador_in],
			np.fmin(tarjeta_grafica_moderado[tarjeta_grafica_in], 
			placa_madre_bueno[placa_madre_in]))))

	regla8 =np.fmin(sistema_refrigeracion_malo[sistema_refrigeracion_in],
			np.fmin(ram_malo[ram_in], 
			np.fmin(procesador_malo[procesador_in],
			placa_madre_malo[placa_madre_in])))

	

	# Se compone la regla con el consecuente
	imp1= np.fmin(regla1,rendimiento_deficiente)
	imp2= np.fmin(regla2,rendimiento_bueno)
	imp3= np.fmin(regla3,rendimiento_bueno)
	imp4= np.fmin(regla4,rendimiento_moderado)
	imp5= np.fmin(regla5,rendimiento_optimo)
	imp6= np.fmin(regla6,rendimiento_malo)
	imp7= np.fmin(regla7,rendimiento_moderado)
	imp8 = np.fmin(regla8, rendimiento_malo)

	# Rendimiento inicial (cero)
	rendimiento0 = np.zeros_like(x_rendimiento)

	##################################################################################################################################
	# Se grafican las reglas con la entrada inicial
	fig3, ax0 = plt.subplots(nrows=1, figsize=(8, 3))

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
	ax0.fill_between(x_rendimiento, rendimiento0, imp8, facecolor='y', alpha=0.7)
	ax0.plot(x_rendimiento, rendimiento_moderado, 'k', linewidth=0.5, linestyle='--')
	ax0.set_ylabel("Grado de pertenencia")
	ax0.set_xlabel("Grado de rendimiento (Puntuación)")
	ax0.set_title('Nivel de rendimiento')

	# Se hacen invisibles las lineas de arriba y la derecha
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.get_xaxis().tick_bottom()
	ax.get_yaxis().tick_left()


	# Se unen todas las reglas
	aggregate_membership = np.fmax(imp1, np.fmax(imp2, np.fmax(imp3, np.fmax(imp4,
									np.fmax(imp5, np.fmax(imp6, np.fmax(imp7, imp8)))))))

	# Se desfucifica utilizando centroide y bisector
	if areaZero(aggregate_membership):
		return dict(error = 1)

	else:
		# Se calcula el centroide para desfuzificar (COA)
		rendimiento_COA = fuzz.defuzz(x_rendimiento, aggregate_membership, 'centroide')
		rendimiento_plot_COA = fuzz.interp_membership(x_rendimiento, aggregate_membership, rendimiento_COA)  # for plot

		# Se calcula el centroide para desfuzificar (BOA)
		rendimiento_BOA = fuzz.defuzz(x_rendimiento, aggregate_membership, 'bisector')
		rendimiento_plot_BOA = fuzz.interp_membership(x_rendimiento, aggregate_membership, rendimiento_BOA)  # for plot

		# Se visualiza el grafico
		fig4, (ax0, ax1) = plt.subplots(nrows=2, figsize=(8, 12))

		ax0.plot(x_rendimiento, rendimiento_malo, 'b', linewidth=0.5, linestyle='--')
		ax0.plot(x_rendimiento, rendimiento_deficiente, 'g', linewidth=0.5, linestyle='--')
		ax0.plot(x_rendimiento, rendimiento_moderado, 'r', linewidth=0.5, linestyle='--')
		ax0.plot(x_rendimiento, rendimiento_bueno, 'm', linewidth=0.5, linestyle='--')
		ax0.plot(x_rendimiento, rendimiento_optimo, c='darkorange', linewidth=0.5, linestyle='--')
		ax0.fill_between(x_rendimiento, rendimiento0, aggregate_membership, facecolor='Orange', alpha=0.7)
		ax0.plot([rendimiento_COA, rendimiento_COA], [0, rendimiento_plot_COA], 'k', linewidth=1.5, alpha=0.9)
		ax0.set_title('Resultado al desfuzificar con COA')

		ax1.plot(x_rendimiento, rendimiento_malo, 'b', linewidth=0.5, linestyle='--')
		ax1.plot(x_rendimiento, rendimiento_deficiente, 'g', linewidth=0.5, linestyle='--')
		ax1.plot(x_rendimiento, rendimiento_moderado, 'r', linewidth=0.5, linestyle='--')
		ax1.plot(x_rendimiento, rendimiento_bueno, 'm', linewidth=0.5, linestyle='--')
		ax1.plot(x_rendimiento, rendimiento_optimo, c='darkorange', linewidth=0.5, linestyle='--')
		ax1.fill_between(x_rendimiento, rendimiento0, aggregate_membership, facecolor='Orange', alpha=0.7)
		ax1.plot([rendimiento_BOA, rendimiento_BOA], [0, rendimiento_plot_BOA], 'k', linewidth=1.5, alpha=0.9)
		ax1.set_title('Resultado al desfuzificar con BOA')

	# Se hacen invisibles las lineas de arriba y la derecha
		for ax in (ax0, ax1):
			ax.set_ylabel("Grado de pertenencia")
			ax.set_xlabel("Grado de rendimiento (Puntuación)")
			ax.spines['top'].set_visible(False)
			ax.spines['right'].set_visible(False)
			ax.get_xaxis().tick_bottom()
			ax.get_yaxis().tick_left()

		# COA
		rendimiento_result_malo = fuzz.interp_membership(x_rendimiento, rendimiento_malo, rendimiento_COA)
		rendimiento_result_deficiente = fuzz.interp_membership(x_rendimiento, rendimiento_deficiente, rendimiento_COA)
		rendimiento_result_moderado = fuzz.interp_membership(x_rendimiento, rendimiento_moderado, rendimiento_COA)
		rendimiento_result_bueno = fuzz.interp_membership(x_rendimiento, rendimiento_bueno, rendimiento_COA)
		rendimiento_result_optimo = fuzz.interp_membership(x_rendimiento, rendimiento_optimo, rendimiento_COA)

		valorPertenenciaCOA, resultPositionCOA = maxAndPos([rendimiento_result_malo, 
													 rendimiento_result_deficiente, 
													 rendimiento_result_moderado, 
													 rendimiento_result_bueno, 
													 rendimiento_result_optimo])
		rendimiento_estimacion_COA = interpretateRendimiento(resultPositionCOA)

		# BOA
		rendimiento_result_malo = fuzz.interp_membership(x_rendimiento, rendimiento_malo, rendimiento_BOA)
		rendimiento_result_deficiente = fuzz.interp_membership(x_rendimiento, rendimiento_deficiente, rendimiento_BOA)
		rendimiento_result_moderado = fuzz.interp_membership(x_rendimiento, rendimiento_moderado, rendimiento_BOA)
		rendimiento_result_bueno = fuzz.interp_membership(x_rendimiento, rendimiento_bueno, rendimiento_BOA)
		rendimiento_result_optimo = fuzz.interp_membership(x_rendimiento, rendimiento_optimo, rendimiento_BOA)

		valorPertenenciaBOA, resultPositionBOA = maxAndPos([rendimiento_result_malo, 
													 rendimiento_result_deficiente, 
													 rendimiento_result_moderado, 
													 rendimiento_result_bueno, 
													 rendimiento_result_optimo])
		rendimiento_estimacion_BOA = interpretateRendimiento(resultPositionBOA)

		#print("En base a los datos ingresados, y al 'valor de pertenencia' obtenido (",valorPertenencia,").\nEs que se estima que padece",rendimiento_estimacion)

	return dict(coa = [valorPertenenciaCOA, rendimiento_estimacion_COA],
				boa = [valorPertenenciaBOA, rendimiento_estimacion_BOA],
				error = 0)
