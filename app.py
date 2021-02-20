from tkinter import *
from tkinter import messagebox
import fuzzymodel as fm
from PIL import ImageTk, Image
import matplotlib.pyplot as plt 

# Funcion que verifica si la puntuacion de string es un numero retorna True, en caso contrario  False 
# Entrada: Un string
# Salida: booleano
def is_valid_int(int_string):
    try:
        int_string= int(int_string)
        if(int_string>=0 and int_string<=12):
            return True
        else:
            return False
    except ValueError:
        return False

# Función que verifica las entradas que ingresa el usuario
# Entrada: entero (input sistema de refrigeracion)
#          entero (input ram)
#          entero (input procesador)
#		   entero (input placa madre)
#		   entero (input memoria física)
#		   entero (input tarjeta gráfica)
#		   entero (input fuente de poder)
# Salida:  booleano
def calculos(sistema_refrigeracion_in, ram_in, procesador_in, placa_madre_in, memoria_fisica_in, tarjeta_grafica_in, fuente_poder_in):
    sistema_refrigeracion_in=sistema_refrigeracion_in.get()
    if not (is_valid_int(sistema_refrigeracion_in)):
        messagebox.showinfo(message="La puntuacion del sistema de refrigeracion no es válida, vuelva a ingresarlo", title="ERROR")
        return True
    sistema_refrigeracion_in=int(sistema_refrigeracion_in)

    ram_in=ram_in.get()
    if not (is_valid_int(ram_in)):
        messagebox.showinfo(message="La puntuacion de la ram no es válida, vuelva a ingresarlo", title="ERROR")
        return True
    ram_in=int(ram_in)

    procesador_in=procesador_in.get()
    if not (is_valid_int(procesador_in)):
        messagebox.showinfo(message="La puntuacion del procesador no es válida, vuelva a ingresarlo", title="ERROR")
        return True
    procesador_in=int(procesador_in)

    placa_madre_in=placa_madre_in.get()
    if not (is_valid_int(placa_madre_in)):
        messagebox.showinfo(message="La puntuacion de la placa madre no es válida, vuelva a ingresarlo", title="ERROR")
        return True
    placa_madre_in=int(placa_madre_in)


    memoria_fisica_in=memoria_fisica_in.get()
    if not (is_valid_int(memoria_fisica_in)):
        messagebox.showinfo(message="La puntuacion de la memoria fisica no es válida, vuelva a ingresarlo", title="ERROR")
        return True
    memoria_fisica_in=int(memoria_fisica_in)

    tarjeta_grafica_in=tarjeta_grafica_in.get()
    if not (is_valid_int(tarjeta_grafica_in)):
        messagebox.showinfo(message="La puntuacion de la tarjeta gráfica no es válida, vuelva a ingresarlo", title="ERROR")
        return True
    tarjeta_grafica_in=int(tarjeta_grafica_in)

    fuente_poder_in=fuente_poder_in.get()
    if not (is_valid_int(fuente_poder_in)):
        messagebox.showinfo(message="La puntuacion de la fuente de poder no es válida, vuelva a ingresarlo", title="ERROR")
        return True
    fuente_poder_in=int(fuente_poder_in)

    resultado = fm.fuzzy_model(sistema_refrigeracion_in,ram_in,procesador_in,placa_madre_in,memoria_fisica_in,tarjeta_grafica_in,fuente_poder_in)
    
    InterfazResultado(resultado)
    return True
#Función que borra la venta de resultados y los graficos
#Entrada: ventana de tkinter
#Salida: -
def consultar_otra_vez(ventana_resultado):
    plt.close('all')
    ventana_resultado.destroy()
# Función que genera una ventana con los resultados
# Entrada: diccionario (resultados)
# Salida: -
def InterfazResultado(resultado):
    ventana_resultado = Tk()
    ventana_resultado.geometry()
    ventana_resultado.title("Consultas")
    ventana_resultado.wm_iconbitmap("imgs/1.ico")
    titulo = Label(ventana_resultado, text="Resultados Obtenidos", font=("Arial Bold", 13), relief= "groove")


    if(resultado["error"] == 0):
        titulo.grid(column= 0, row= 0, columnspan=2, pady=5)
        labelCOA = Label(ventana_resultado, text="Resultado calculado con centro de área (COA)", font=("Arial Bold",11), fg= "gray10")
        labelCOA.grid(column= 0, row= 1, columnspan=2)

        nivelRendimientoCOALabel = Label(ventana_resultado, text="Nivel de Rendimiento: ", font=("Arial Bold", 10),  fg= "gray10",anchor= "w")
        nivelRendimientoCOALabel.grid(column= 0, row= 2 ,padx=4)
        nivelRendimientoCOA = Label(ventana_resultado, text=str(resultado["coa"][1]), font=("Arial Bold", 10),  fg= "gray10", relief= "ridge",anchor= "w")
        nivelRendimientoCOA.grid(column= 1, row= 2,sticky= "nesw")

        pertenenciaCOALabel = Label(ventana_resultado, text="Porcentaje de Pertenencia: ", font=("Arial Bold", 10),  fg= "gray10",anchor= "w")
        pertenenciaCOALabel.grid(column= 0, row= 3,padx=4)
        pertenenciaCOA = Label(ventana_resultado, text=str(float(resultado["coa"][0])*100)+"%", font=("Arial Bold", 10),  fg= "gray10", relief= "ridge",anchor= "w")
        pertenenciaCOA.grid(column= 1, row= 3,sticky= "nesw")

        espacio1 = Label(ventana_resultado, text="", pady=5)
        espacio1.grid(column= 0, row=4)

        labelBOA = Label(ventana_resultado, text="Resultado calculado con bisector de área (BOA)", font=("Arial Bold",11))
        labelBOA.grid(column= 0, row= 5, columnspan=4, sticky= "nw")

        nivelRendimientoBOALabel = Label(ventana_resultado, text="Nivel de Rendimiento: ", font=("Arial Bold", 10),  fg= "gray10",anchor= "w")
        nivelRendimientoBOALabel.grid(column= 0, row= 7,padx=4)
        nivelRendimientoBOA = Label(ventana_resultado, text=str(resultado["boa"][1]), font=("Arial Bold", 10),  fg= "gray10", relief= "ridge",anchor= "w")
        nivelRendimientoBOA.grid(column= 1, row= 7,sticky= "nesw")

        pertenenciaBOALabel = Label(ventana_resultado, text="Porcentaje de Pertenencia: ", font=("Arial Bold", 10),  fg= "gray10",anchor= "w")
        pertenenciaBOALabel.grid(column= 0, row= 8,padx=4)
        pertenenciaBOA = Label(ventana_resultado, text=str(float(resultado["boa"][0])*100)+"%", font=("Arial Bold", 10),  fg= "gray10", relief= "ridge",anchor= "w")
        pertenenciaBOA.grid(column= 1, row= 8,sticky= "nesw")
        graficosBoton=Button(ventana_resultado,text="Ver Gráficos",command=lambda: plt.show())
        graficosBoton.grid(column= 0, row= 13, sticky="nesw", pady=10)

        salir=Button(ventana_resultado,text="Consultar de nuevo",command=lambda:consultar_otra_vez(ventana_resultado) )
        salir.grid(column= 1, row= 13,sticky="nesw", pady = 10)
    
    else:
        titulo.grid(column= 0, row= 0, columnspan=4, pady=5)
        labelCOA = Label(ventana_resultado, text="El resultado de la desfucificación es 0\nNo se ha encontrado el nivel de rendimiento\nSe recomienda consultar con un profesional", font=("Arial Bold",12), fg= "gray10",justify="center")
        labelCOA.grid(column= 0, row= 1, columnspan=4, sticky= "nw")

        graficosBoton=Button(ventana_resultado,text="Ver Gráficos",command=lambda: plt.show())
        graficosBoton.grid(column= 0, row= 13, columnspan=2, sticky="nesw", pady=10)

        salir=Button(ventana_resultado,text="Consultar de nuevo",command=lambda: consultar_otra_vez(ventana_resultado))
        salir.grid(column= 2, row= 13, columnspan=2,sticky="nesw", pady = 10)

    ventana_resultado.mainloop()

# Función que genera la ventana inicial para interactuar con el usuario
# Entrada: - 
# Salida: -
def InicializarInterfaz():
    # inicio de interfaz
    ventana = Tk()
    var = IntVar()
    ventana.geometry("470x320")
    ventana.title("Consultas")
    ventana.wm_iconbitmap("imgs/1.ico")
    img= Image.open("imgs/logicadifusa.jpg")
    img= img.resize((120,120))
    img = ImageTk.PhotoImage(img)
    
    panel = Label(ventana, image = img)
    panel.grid(column= 3,row= 4, rowspan= 5)

    # Barra de menu
    menubar = Menu(ventana)
    ventana.config(menu=menubar)
    filemenu = Menu(menubar)
    helpmenu = Menu(menubar)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Salir", command=ventana.quit)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Instrucciones")
    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)

    
    # Titulo
    titulo = Label(ventana, text="Bienvenido, al Diagnosticador de Hardware", font=("Arial Bold", 15), relief= "groove", fg= "gray1")
    titulo.grid(column= 0, row= 0, columnspan=4, sticky= "nsew", pady=5)

    descripcion = Label(ventana, text="Del 0 al 12 que tan bien funcionan los siguientes componentes (Numeros Enteros)", font=("Arial Bold",9), fg= "gray10")
    descripcion.grid(column= 0, row= 1, columnspan=4, sticky= "nw")


    sistema_refrigeracion_label = Label(ventana, text="Sistema refrigeracion", font=("Arial Bold", 11),  fg= "gray10", relief= "ridge",anchor= "w")
    sistema_refrigeracion_label.grid(column= 0, row= 3, sticky= "nesw",padx=4)
    sistema_refrigeracion_in=Entry(ventana,width= 3)
    sistema_refrigeracion_in.grid(column= 1, row= 3,sticky= "nesw")

    ram_label = Label(ventana, text="Ram", font=("Arial Bold", 11),  fg= "gray10", relief= "ridge",anchor= "w")
    ram_label.grid(column= 0, row= 4, sticky= "nesw", padx=4)
    ram_in=Entry(ventana,width= 4)
    ram_in.grid(column= 1, row= 4,sticky= "nesw")

    procesador_label = Label(ventana, text="Procesador", font=("Arial Bold", 11),  fg= "gray10", relief= "ridge",anchor= "w")
    procesador_label.grid(column= 0, row= 5, sticky= "nesw", padx=4)
    procesador_in=Entry(ventana,width= 5)
    procesador_in.grid(column= 1, row= 5,sticky= "nesw")

    placa_madre_label = Label(ventana, text="Placa madre", font=("Arial Bold", 11),  fg= "gray10", relief= "ridge",anchor= "w")
    placa_madre_label.grid(column= 0, row= 6, sticky= "nesw", padx=4)
    placa_madre_in=Entry(ventana,width= 6)
    placa_madre_in.grid(column= 1, row= 6,sticky= "nesw")

    memoria_fisica_label = Label(ventana, text="Memoria fisica", font=("Arial Bold", 11),  fg= "gray10", relief= "ridge",anchor= "w")
    memoria_fisica_label.grid(column= 0, row= 7, sticky= "nesw", padx=4)
    memoria_fisica_in=Entry(ventana,width= 7)
    memoria_fisica_in.grid(column= 1, row= 7,sticky= "nesw")

    tarjeta_grafica_label = Label(ventana, text="Tarjeta grafica", font=("Arial Bold", 11),  fg= "gray10", relief= "ridge",anchor= "w")
    tarjeta_grafica_label.grid(column= 0, row= 8, sticky= "nesw", padx=4)
    tarjeta_grafica_in=Entry(ventana,width= 8)
    tarjeta_grafica_in.grid(column= 1, row= 8,sticky= "nesw")

    fuente_poder_label = Label(ventana, text="Fuente poder", font=("Arial Bold", 11),  fg= "gray10", relief= "ridge",anchor= "w")
    fuente_poder_label.grid(column= 0, row= 9, sticky= "nesw", padx=4)
    fuente_poder_in=Entry(ventana,width= 9)
    fuente_poder_in.grid(column= 1, row= 9,sticky= "nesw")

    calcular=Button(ventana,text="Consultar",command=lambda: calculos(sistema_refrigeracion_in, ram_in, procesador_in, placa_madre_in, memoria_fisica_in, tarjeta_grafica_in, fuente_poder_in))
    calcular.grid(column= 3, row= 10, sticky="nesw")
    
    calcular=Button(ventana,text="Salir",command=lambda: salir(ventana))
    calcular.grid(column= 3, row= 11, sticky="nesw", pady=7)
    

    # Mostrar interfaz
    ventana.mainloop()

def salir(ventana):
    ventana.destroy()
    exit()
