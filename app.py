from tkinter import *

# Se crea la ventana principal
ventana = Tk()

def InicializarInterfaz():
    # inicio de interfaz
    var = IntVar()
    ventana.geometry("800x460")
    ventana.title("Consultas")
    ventana.wm_iconbitmap("1.ico")

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
    titulo = Label(ventana, text="Bienvenido, al Diagnosticador de Hardware", font=("Arial Bold", 15))
    titulo.grid(column= 0, row = 0, sticky = W, pady=5)

    # Mostrar interfaz
    ventana.mainloop()