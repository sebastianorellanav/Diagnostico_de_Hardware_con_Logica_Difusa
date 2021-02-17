import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt 

def category(x, malo, deficiente, moderado, bueno, optimo, inp):
    refrigeracion_cat_malo = fuzz.interp_membership(x, malo, inp) 
    refrigeracion_cat_deficiente = fuzz.interp_membership(x, deficiente, inp)
    refrigeracion_cat_moderado = fuzz.interp_membership(x, moderado, inp) 
    refrigeracion_cat_bueno = fuzz.interp_membership(x, bueno, inp) 
    refrigeracion_cat_optimo = fuzz.interp_membership(x, optimo, inp) 
    return dict(malo = refrigeracion_cat_malo, 
                deficiente = refrigeracion_cat_deficiente,
                moderado = refrigeracion_cat_moderado,
                bueno = refrigeracion_cat_bueno,
                optimo = refrigeracion_cat_optimo)
