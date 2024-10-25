import tkinter as tk
from cProfile import label
from tkinter import *
from graphviz import Graph, render
from PIL import Image, ImageTk
from tkinter import messagebox

dot = Graph(comment='Ejemplo Grafo')
img1 = None
label_frame = None
label_frameVertice = None
# Lista de Vertices

lista_Vertices = []
lista_Aristas = []

# Creando Ventana
ventana = tk.Tk()
ventana.title("Proyecto Grafos")
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ancho_ventana = 800  # Ancho deseado
alto_ventana = 800  # Alto deseado

# Posicion de la ventana
pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")


# Funciones
# Crear Vertices

def crear_vertice(nombreVertice):
    if nombreVertice == "":
        print("Necesita agregar el nombre del vertice")

    else:
        if nombreVertice in lista_Vertices:
            mensaje(f'El vertice "{nombreVertice.upper()}"  ya existe')
        else:
            # dot.node(nombreVertice.upper(),nombreVertice.upper())
            lista_Vertices.append(nombreVertice)
            recorrer_listaVertices()


# Crear Aristas
def crear_arista(vertice1, vertice2):
    if vertice1 and vertice2 in lista_Vertices:
        aristaNueva = vertice1 + vertice2
        if aristaNueva not in lista_Aristas:
            lista_Aristas.append(aristaNueva)
            dot.edge(f'{vertice1.upper()}', f'{vertice2.upper()}')
        else:
            mensaje(f'La arista "{aristaNueva.upper()}"  ya existe')


    else:
        mensaje('Los Vertices Ingresados No Existen')


# Crear Imagen Grafo
def imagen():
    global img1
    global contador
    if len(lista_Vertices) > 0:

        i1 = dot.render('grafo', format='png', cleanup=TRUE)
        img = Image.open(i1)
        render = ImageTk.PhotoImage(img)
        if img1 is not None:
            img1.destroy()

        img1 = Label(ventana, image=render)
        img1.image = render
        img1.place(x=50, y=50)
        recorrer_listaArista()

    else:
        mensaje("No hay grafo para mostrar")


# Actualizar las aristas

def crearetiquetas(numero, arista):
    nombre_aristas = tk.Label(ventana, width=25, text=f'#{numero}. {arista}')
    nombre_aristas.grid(row=numero, column=4, padx=10, pady=10)


def recorrer_listaVertices():
    global label_frameVertice

    if label_frameVertice is not None:
        label_frameVertice.destroy()

    label_frameVertice = tk.LabelFrame(ventana, text="--Vertices--", width=25)
    label_frameVertice.place(x=400, y=570)

    for numero, vertice in enumerate(lista_Vertices):
        nombre_label = tk.Label(label_frameVertice, text=f"{vertice.upper()}")
        nombre_label.grid(row=numero, column=0, sticky='w')


def recorrer_listaArista():
    global label_frame
    if label_frame is not None:
        label_frame.destroy()

    label_frame = tk.LabelFrame(ventana, text="--Aristas--", width=25)
    label_frame.place(x=500, y=570)

    for numero, arista in enumerate(lista_Aristas):
        aristasSeparadas = list(arista.upper())
        A1, A2 = aristasSeparadas[0], aristasSeparadas[1]
        nombre_label = tk.Label(label_frame, text=f"{A1}-{A2}")
        nombre_label.grid(row=numero, column=0, sticky='w')


# Mensaje de Error
def mensaje(infoM):
    messagebox.showwarning("showinfo", infoM)


# Obtener los datos del vertice
def on_button_click():
    textoVertice = txt_vertice.get()
    crear_vertice(textoVertice)


# Ingresar los datos para la arista
def on_button_click2():
    textoArista = txt_arista.get().split('-')
    if len(textoArista) < 2:
        mensaje('Debe ingresar dos Vertices para crear una Arista')
    else:
        v1, v2 = textoArista
        crear_arista(v1, v2)


# Creacion de un input

ventana.grid_rowconfigure(0, weight=50)
# ********************************************Vertice
txt_vertice = tk.Entry(ventana, width=25)
txt_vertice.grid(row=3, column=2, padx=10, pady=10)

# Boton Vertice
boton_vertice = tk.Button(ventana, text="Agregar Vertice", command=on_button_click)
boton_vertice.grid(row=3, column=1, padx=10, pady=10)

# *******************************************Arista
# Boton Arista
txt_arista = tk.Entry(ventana, width=25)
txt_arista.grid(row=4, column=2, padx=10, pady=10)

boton_arista = tk.Button(ventana, text="Agregar Arista ", command=on_button_click2)
boton_arista.grid(row=4, column=1, padx=10, pady=10)  # Fila 0, columna 0

# *****************************Boton Grafo
boton_grafo = tk.Button(ventana, text="Mostrar El Grafo ", command=imagen)
boton_grafo.grid(row=5, column=1, padx=10, pady=50)

ventana.mainloop()
