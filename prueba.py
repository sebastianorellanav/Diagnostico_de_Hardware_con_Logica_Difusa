import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt 

########## INPUTS ########################
#Input Universe functions
servicio = np.arange(0,11,.1)
comida    = np.arange(0,11,.1)
# Input Membership Functions
# Service
servicio_malo = fuzz.gaussmf(servicio ,0,1.5)
servicio_bueno = fuzz.gaussmf(servicio ,5,1.5)
servicio_excelente = fuzz.gaussmf(servicio ,10,1.5)
# Food
comida_mala = fuzz.trapmf(comida , [0, 0, 1, 3])
comida_buena = fuzz.gaussmf(comida ,10,1.5)

########## OUTPUT ########################
# Tip
# Output Variables Domain
propina = np.arange(0,30,.1)
# Output  Membership Function 
propina_mala  = fuzz.trimf(propina, [0, 5, 10])
propina_media = fuzz.trimf(propina, [10, 15, 25])
propina_buena = fuzz.trimf(propina, [20, 25, 30])


def food_category(comida_input = 2):
    comida_cat_mala = fuzz.interp_membership(comida, comida_mala, comida_input) # Depends from Step 1
    comida_cat_buena = fuzz.interp_membership(comida,comida_buena,comida_input) # Depends form Step 1
    return dict(rancid = comida_cat_mala, delicious = comida_cat_buena)

def service_category(servicio_input = 4):
    servicio_cat_malo = fuzz.interp_membership(servicio,servicio_malo, servicio_input) # Depends from Step 1
    servicio_cat_buena = fuzz.interp_membership(servicio,servicio_malo, servicio_input)
    servicio_cat_excelente = fuzz.interp_membership(servicio,servicio_excelente, servicio_input)
    return dict(poor = servicio_cat_malo, good = servicio_cat_buena, excellent = servicio_cat_excelente)


#Exaple input variables 
comida_input = food_category(2.34)
servicio_input = service_category(1.03)
print ("For Service "+str(servicio_input))
print ("For Food "+ str(comida_input)) 

#Step 3: Determine the weight for each rule from fuzzy antecents
rule1 = np.fmax(servicio_input['poor'],comida_input['rancid'])
rule2 = servicio_input['good']
rule3 = np.fmax(comida_input['delicious'],servicio_input['excellent'])


#Step 4: Apply implication opetator (Mamdami - min):
imp1 = np.fmin(rule1,propina_mala)
imp2 = np.fmin(rule2,propina_media)
imp3 = np.fmin(rule3,propina_media)


#Step 5: Aggregate all output - max
aggregate_membership = np.fmax(imp1, np.fmax(imp2,imp3))


#Step 6: Defuzzify using Centroid
result_tip = fuzz.defuzz(tip, aggregate_membership , 'centroid')
print result_tip