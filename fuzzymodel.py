import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt 
import fuzzyfunctions as ff 
def fuzzy_model(sistema_refrigeracion_in, ram_in, procesador_in, placa_madre_in, memoria_fisica_in, tarjeta_grafica_in, fuente_poder_in):
	########## INPUTS ########################
	#Input Universe functions

	x_sistema_refrigeracion = np.arange(0, 10.1, .1)
	x_ram = np.arange(0, 10.1, .1)
	x_procesador  = np.arange(0, 10.1, .1)
	x_placa_madre = np.arange(0,10.1,.1)
	x_memoria_fisica = np.arange(0,10.1,.1)
	x_tarjeta_grafica = np.arange(0,10.1,.1)
	x_fuente_poder = np.arange(0,10.1,.1)
	x_rendimiento = np.arange(0,10.1,.1)

	# Input Membership Functions
	# sistema de refrigeracion
	sistema_refrigeracion_malo = fuzz.trapmf(x_sistema_refrigeracion, [0, 0, 1, 2])
	sistema_refrigeracion_deficiente = fuzz.trapmf(x_sistema_refrigeracion, [1, 2, 4, 5])
	sistema_refrigeracion_moderado = fuzz.trapmf(x_sistema_refrigeracion, [3, 6, 7, 8])
	sistema_refrigeracion_bueno = fuzz.trapmf(x_sistema_refrigeracion, [6.5, 7.5, 8, 9])
	sistema_refrigeracion_optimo = fuzz.trapmf(x_sistema_refrigeracion, [8, 9, 10, 10])


	# ram
	ram_malo = fuzz.trapmf(x_ram, [0, 0, 1, 3])
	ram_deficiente = fuzz.trapmf(x_ram, [1.5, 3, 3.5, 5])
	ram_moderado = fuzz.trapmf(x_ram, [3, 4, 5, 6])
	ram_bueno = fuzz.trapmf(x_ram, [4.5, 5, 7, 8])
	ram_optimo = fuzz.trapmf(x_ram, [6, 8, 10, 10])

	# procesador
	procesador_malo = fuzz.trapmf(x_procesador, [0, 0, 2, 2.3])
	procesador_deficiente = fuzz.trapmf(x_procesador, [1, 3, 3.5, 4])
	procesador_moderado = fuzz.trapmf(x_procesador, [3, 4.5, 6, 8])
	procesador_bueno = fuzz.trapmf(x_procesador, [5, 6.5, 7.5, 9])
	procesador_optimo = fuzz.trapmf(x_procesador, [7, 8, 10, 10])

	# placa madre
	placa_madre_malo = fuzz.trapmf(x_placa_madre, [0, 0, 1, 3])
	placa_madre_deficiente = fuzz.trapmf(x_placa_madre, [1, 2, 4, 5])
	placa_madre_moderado = fuzz.trapmf(x_placa_madre, [4, 6, 7, 8])
	placa_madre_bueno = fuzz.trapmf(x_placa_madre, [6.5, 7.5, 8, 9])
	placa_madre_optimo = fuzz.trapmf(x_placa_madre, [7.5, 9, 10, 10])

# memoria fisica
	memoria_fisica_malo = fuzz.trapmf(x_memoria_fisica, [0, 0, 2, 3])
	memoria_fisica_deficiente = fuzz.trapmf(x_memoria_fisica, [2, 3, 3.5, 4])
	memoria_fisica_moderado = fuzz.trapmf(x_memoria_fisica, [3.5, 4, 5.5, 6])
	memoria_fisica_bueno = fuzz.trapmf(x_memoria_fisica, [5.5, 6, 7.0, 7.5])
	memoria_fisica_optimo = fuzz.trapmf(x_memoria_fisica, [7, 7.5,10, 10])

	# tarjeta grafica
	tarjeta_grafica_malo = fuzz.trapmf(x_tarjeta_grafica, [0, 0, 2, 3])
	tarjeta_grafica_deficiente = fuzz.trapmf(x_tarjeta_grafica, [2, 3, 5, 6])
	tarjeta_grafica_moderado = fuzz.trapmf(x_tarjeta_grafica, [5, 6,6.5, 7])
	tarjeta_grafica_bueno = fuzz.trapmf(x_tarjeta_grafica, [6.5, 7, 7.5, 8])
	tarjeta_grafica_optimo = fuzz.trapmf(x_tarjeta_grafica, [7.5, 8, 10, 10])

	# fuente poder
	fuente_poder_malo = fuzz.trapmf(x_fuente_poder, [0, 2, 2, 3])
	fuente_poder_deficiente = fuzz.trapmf(x_fuente_poder, [2, 3, 5, 5.5])
	fuente_poder_moderado = fuzz.trapmf(x_fuente_poder, [5, 5.5, 6 ,7 ])
	fuente_poder_bueno = fuzz.trapmf(x_fuente_poder, [6, 7, 8, 9])
	fuente_poder_optimo = fuzz.trapmf(x_fuente_poder, [8, 9, 10, 10])


	# rendimiento
	rendimiento_malo = fuzz.trapmf(x_rendimiento, [0, 0, 1.5, 2])
	rendimiento_deficiente = fuzz.trapmf(x_rendimiento, [1.5, 2, 3, 3.5])
	rendimiento_moderado = fuzz.trapmf(x_rendimiento, [3, 3.5, 4, 4.5 ])
	rendimiento_bueno = fuzz.trapmf(x_rendimiento, [4, 4.5, 7, 8])
	rendimiento_optimo = fuzz.trapmf(x_rendimiento, [7, 8, 10, 10])

	sistema_refrigeracion_input = ff.category(x_sistema_refrigeracion,
	                                          sistema_refrigeracion_malo,
	                                          sistema_refrigeracion_deficiente,
	                                          sistema_refrigeracion_moderado,
	                                          sistema_refrigeracion_bueno,
	                                          sistema_refrigeracion_optimo,
	                                          sistema_refrigeracion_in)

	ram_input = ff.category(x_ram,
	                        ram_malo,
	                        ram_deficiente,
	                        ram_moderado,
	                        ram_bueno,
	                        ram_optimo,
	                        ram_in)


	procesador_input = ff.category(x_procesador,
	                               procesador_malo,
	                               procesador_deficiente,
	                               procesador_moderado,
	                               procesador_bueno,
	                               procesador_optimo,
	                               procesador_in)

	placa_madre_input = ff.category(x_placa_madre,
	                                placa_madre_malo,
	                                placa_madre_deficiente,
	                                placa_madre_moderado,
	                                placa_madre_bueno,
	                                placa_madre_optimo,
	                                placa_madre_in)


	memoria_fisica_input = ff.category(x_memoria_fisica,
	                                   memoria_fisica_malo,
	                                   memoria_fisica_deficiente,
	                                   memoria_fisica_moderado,
	                                   memoria_fisica_bueno,
	                                   memoria_fisica_optimo,
	                                   memoria_fisica_in)

	tarjeta_grafica_input = ff.category(x_tarjeta_grafica,
	                                    tarjeta_grafica_malo,
	                                    tarjeta_grafica_deficiente,
	                                    tarjeta_grafica_moderado,
	                                    tarjeta_grafica_bueno,
	                                    tarjeta_grafica_optimo,
	                                    tarjeta_grafica_in)
	                            
	fuente_poder_input = ff.category(x_fuente_poder,
	                                 fuente_poder_malo,
	                                 fuente_poder_deficiente,
	                                 fuente_poder_moderado,
	                                 fuente_poder_bueno,
	                                 fuente_poder_optimo,
	                                 fuente_poder_in)


	#Step 3: Determine the weight for each rule from fuzzy antecents
	regla1 = np.fmin(sistema_refrigeracion_input['deficiente'],
	                 np.fmin(ram_input['deficiente'], 
	                 np.fmin(procesador_input['deficiente'],
	                 np.fmin(tarjeta_grafica_input['deficiente'], 
	                 fuente_poder_input['moderado']))))

	regla2 = np.fmin(sistema_refrigeracion_input['malo'],
	                 np.fmin(ram_input['moderado'], 
	                 np.fmin(procesador_input['moderado'],
	                 np.fmin(placa_madre_input['bueno'], 
	                 np.fmin(tarjeta_grafica_input['moderado'],
	                 fuente_poder_input['bueno'])))))

	regla3 = np.fmin(placa_madre_input['optimo'],
	                 np.fmin(ram_input['moderado'], 
	                 np.fmin(procesador_input['optimo'],
	                 fuente_poder_input['moderado'])))

	regla4 = np.fmax(placa_madre_input['moderado'],
	                 np.fmax(sistema_refrigeracion_input['optimo'], 
	                 np.fmax(memoria_fisica_input['bueno'],
	                 fuente_poder_input['moderado'])))

	regla5 = np.fmin(ram_input['optimo'], placa_madre_input['optimo'])

	regla6 = np.fmin(np.fmax(placa_madre_input['deficiente'],
	                         sistema_refrigeracion_input['moderado']),
	                 np.fmax(procesador_input['bueno'],
	                         ram_input['bueno']))

	regla7 = np.fmin(sistema_refrigeracion_input['optimo'],
	                 np.fmin(ram_input['moderado'], 
	                 np.fmin(procesador_input['moderado'],
	                 np.fmin(tarjeta_grafica_input['moderado'], 
	                 placa_madre_input['bueno']))))


	#Step 4: Apply implication opetator (Mamdami - min):
	imp1 = np.fmin(regla1, rendimiento_deficiente)
	imp2 = np.fmin(regla2, rendimiento_bueno)
	imp3 = np.fmin(regla3, rendimiento_bueno)
	imp4 = np.fmin(regla4, rendimiento_moderado)
	imp5 = np.fmin(regla5, rendimiento_optimo)
	imp6 = np.fmin(regla6, rendimiento_malo)
	imp7 = np.fmin(regla7, rendimiento_moderado)


	#Step 5: Aggregate all output - max
	aggregate_membership = np.fmax(imp1, np.fmax(imp2, np.fmax(imp3, np.fmax(imp4,
	                               np.fmax(imp5, np.fmax(imp6, imp7))))))

	#Step 6: Defuzzify using Centroid
	resultado_COA = fuzz.defuzz(x_rendimiento, aggregate_membership , 'centroid')
	print(resultado_COA)

	resultado_BOA = fuzz.defuzz(x_rendimiento, aggregate_membership , 'bisector')
	print(resultado_BOA)
	return [resultado_BOA,resultado_COA]
