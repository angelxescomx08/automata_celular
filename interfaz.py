from tkinter import Tk,Menu,Label,Entry,Button
from automata import crear_matriz_hilos
from tkinter.filedialog import askopenfilename,asksaveasfile
from archivo import cargar_archivo,guardar_archivo,binarizar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk) 
from matplotlib.figure import Figure
from functools import partial
import random
from matplotlib.colors import LinearSegmentedColormap
from tkinter.colorchooser import askcolor
from os.path import exists

class Ventana():
    def __init__(self):
        self.ventana = Tk()
        self.color_uno = "#000000"
        self.color_cero = "#ffffff"
        self.menu = Menu(self.ventana)
        self.fig = Figure(figsize = (8, 8), dpi = 100) 
        self.canvas = FigureCanvasTkAgg(self.fig,master = self.ventana) 

        #datos
        self.iteraciones = 0
        self.r = []
        self.inicial = "0"
        self.num_unos = []
        self.matriz = []

        #colocando menus
        self.ventana.config(menu=self.menu)
        #archivos
        self.op = Menu(self.menu,tearoff=0)
        self.op.add_command(label="Cargar archivo",command=self.cargar_archivo)
        self.op.add_command(label="Guardar archivo",command=self.guardar_archivo)
        self.menu.add_cascade(label="Archivo",menu=self.op)
        #graficar cantidad 1
        self.op1 = Menu(self.menu,tearoff=0)
        self.op1.add_command(label="Graficar cantidad de 1's",command=self.op_cantidad_1)
        self.op1.add_command(label="Graficar cantidad de 0's",command=self.op_cantidad_0)
        self.menu.add_cascade(label="Graficar",menu=self.op1)
        #graficar aleatorio
        self.op2 = Menu(self.menu,tearoff=0)
        self.op2.add_command(label="Crear grafica aleatoria",command=self.ventana_aleatorio)
        self.menu.add_cascade(label="Aleatorio",menu=self.op2)
        #colores
        self.op3 = Menu(self.menu,tearoff=0)
        self.op3.add_command(label="Color de 0",command=self.cambiar_color_cero)
        self.op3.add_command(label="Color de 1",command=self.cambiar_color_uno)
        self.menu.add_cascade(label="Colores",menu=self.op3)

        #zoom y opciones de la grafica
        self.toolbar = NavigationToolbar2Tk(self.canvas,self.ventana) 
        self.toolbar.update()  
        self.canvas.get_tk_widget().pack()

        existe = exists('uno_en_medio.txt')
        if existe:
            especificaciones=cargar_archivo('uno_en_medio.txt')
            self.matriz = crear_matriz_hilos(especificaciones[1],especificaciones[0],especificaciones[2])
            self.pintar(self.matriz)
            self.iteraciones = especificaciones[0]
            self.r = especificaciones[1]
            self.inicial = especificaciones[2]
    
    def cambiar_color_cero(self):
        self.color_cero = askcolor()[1]
        self.pintar(self.matriz)

    def cambiar_color_uno(self):
        self.color_uno = askcolor()[1]
        self.pintar(self.matriz)

    def ventana_aleatorio(self):
        ventana = Tk()
        Label(ventana, text='Numero de iteraciones').pack()
        i = Entry(ventana)
        i.pack()
        Label(ventana, text='Cantidad de celulas').pack()
        c = Entry(ventana)
        c.pack()
        Label(ventana, text='Regla (campo vacio = aleatoriamente)').pack()
        er = Entry(ventana)
        er.pack()
        Label(ventana, text='Probabilidad de unos(campo vacio = 50%)').pack()
        p1 = Entry(ventana)
        p1.pack()
        Button(ventana, text='Aceptar', command=partial(self.aleatorio,ventana,i,c,er,p1)).pack()
        ventana.title('Automata celular')
        ventana.geometry("250x200")
        #ventana.eval('tk::PlaceWindow %s center' % ventana.winfo_pathname(ventana.winfo_id()))
        ventana.resizable(False,False)

    def aleatorio(self,ventana,i,c,er,p1):
        regla = []
        inicial = ""
        if er.get() == "":
            for j in range(8):
                regla.append(random.randint(0,1))
        else:
            if er.get()[0] == "b":
                for j in range(1,len(er.get())):
                    regla.append(int(er.get()[j]))
                if len(regla) < 8:
                    for j in range(0,8-len(regla)):
                        regla.insert(0,0)
            else:
                binario = binarizar(int(er.get()))
                for j in binario:
                    regla.append(int(j))
                if len(regla) < 8:
                    for j in range(0,8-len(regla)):
                        regla.insert(0,0)
        for j in range(int(c.get())):
            if p1.get() == "":
                if random.randint(0,1):
                    inicial+="1"
                else:
                    inicial+="0"
            else:
                if random.randint(0,100)<int(p1.get()):
                    inicial+="1"
                else:
                    inicial+="0"
        self.matriz = crear_matriz_hilos(regla,int(i.get()),inicial)
        self.pintar(self.matriz)
        self.iteraciones = int(i.get())
        self.r = regla
        self.inicial = inicial
        ventana.destroy()

    def op_cantidad_0(self):
        arr = []
        for i in range(len(self.matriz)):
            aux = 0
            for j in range(len(self.matriz[0])):
                if not self.matriz[i][j]:
                    aux += 1
            arr.append(aux)
        plt.title("Cantidad de 0's")
        plt.xlabel("iteracion")
        plt.ylabel("cantidad")
        plt.plot(arr)
        plt.show()

    def op_cantidad_1(self):
        arr = []
        for i in range(len(self.matriz)):
            aux = 0
            for j in range(len(self.matriz[0])):
                if self.matriz[i][j]:
                    aux += 1
            arr.append(aux)
        plt.title("Cantidad de 1's")
        plt.xlabel("iteracion")
        plt.ylabel("cantidad")
        plt.plot(arr)
        plt.show()

    def cargar_archivo(self):
        archivo = askopenfilename()
        if archivo:
            especificaciones=cargar_archivo(archivo)
            self.matriz = crear_matriz_hilos(especificaciones[1],especificaciones[0],especificaciones[2])
            self.pintar(self.matriz)
            self.iteraciones = especificaciones[0]
            self.r = especificaciones[1]
            self.inicial = especificaciones[2]

    def guardar_archivo(self):
        archivo = asksaveasfile(mode='w', defaultextension=".txt")
        if archivo is None: #regresa None si se ha cancelado
            return
        guardar_archivo(archivo,self.iteraciones,self.r,self.inicial)

    def pintar(self,matriz):
        cmap = LinearSegmentedColormap.from_list('mycmap', [self.color_cero, self.color_uno])
        grafica = self.fig.add_subplot(111)
        grafica.imshow(self.matriz,cmap = cmap)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def mostrar(self):
        self.ventana.title('Automata celular')
        self.ventana.configure(width=800,height=800)
        #self.ventana.eval('tk::PlaceWindow %s center' % self.ventana.winfo_pathname(self.ventana.winfo_id()))
        self.ventana.resizable(False,False)
        self.ventana.mainloop()

v =  Ventana()
v.mostrar()