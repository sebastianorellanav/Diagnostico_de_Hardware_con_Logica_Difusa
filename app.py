from tkinter import *
from tkinter import messagebox
import fuzzymodel as fm
from PIL import ImageTk, Image

# Se crea la ventana principal
ventana = Tk()
resultado_COA=0
resultado_BOA=0
#entrada: Un string
#salida: bool
#Si La puntuacion de string es un numero retorna True, en caso contrario  False 
def is_valid_int(int_string):
    try:
        int_string= int(int_string)
        if(int_string>=1 and int_string<=10):
            return True
        else:
            return False
    except ValueError:
        return False



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
    print(sistema_refrigeracion_in,ram_in,procesador_in,placa_madre_in,memoria_fisica_in,tarjeta_grafica_in,fuente_poder_in)

    [resultado_BOA, resultado_COA]= fm.fuzzy_model(sistema_refrigeracion_in,ram_in,procesador_in,placa_madre_in,memoria_fisica_in,tarjeta_grafica_in,fuente_poder_in)
    resultado_BOA="El resultado BOA fue "+str(resultado_BOA)
    resultado_COA="El resultado COA fue "+str(resultado_COA)
    text=resultado_BOA+'\n'+resultado_COA
    messagebox.showinfo(message=text, title="Resultado")
    return True




def InicializarInterfaz():
    # inicio de interfaz
    var = IntVar()
    ventana.geometry("400x300")
    ventana.title("Consultas")
    ventana.wm_iconbitmap("1.ico")
    img= Image.open("logicadifusa.jpg")
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

    descripcion = Label(ventana, text="Del 1 al 10 que tan bien funcionan los siguientes componentes", font=("Arial Bold",9), fg= "gray10")
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
    

    # Mostrar interfaz
    ventana.mainloop()

InicializarInterfaz()