import tkinter as tk
from tkinter import *
import networkx as nx
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
from tkinter import messagebox

# Crear un grafo con networkx
grafo = nx.Graph()
img1 = img2 = img3 = None

# Listas para vértices y aristas
lista_Vertices = []
lista_Aristas = []

# Creando Ventana
ventana = tk.Tk()
ventana.title("Proyecto Grafos con NetworkX")
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ancho_ventana = 1000  # Ancho deseado
alto_ventana = 750  # Alto deseado

# Posicion de la ventana
pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Funciones
# Crear Vértices
def crear_vertice(nombreVertice):
    if nombreVertice == "":
        mensaje("Debe agregar un nombre para el vértice")
    else:
        if nombreVertice in lista_Vertices:
            mensaje(f'El vértice "{nombreVertice}" ya existe')
        else:
            lista_Vertices.append(nombreVertice)
            grafo.add_node(nombreVertice)
            recorrer_listaVertices()

# Crear Aristas
def crear_arista(vertice1, vertice2):
    if vertice1 in lista_Vertices and vertice2 in lista_Vertices:
        if (vertice1, vertice2) not in lista_Aristas and (vertice2, vertice1) not in lista_Aristas:
            lista_Aristas.append((vertice1, vertice2))
            grafo.add_edge(vertice1, vertice2)
        else:
            mensaje(f'La arista "{vertice1}-{vertice2}" ya existe')
    else:
        mensaje('Uno o ambos vértices no existen')

# Mostrar Grafo Original, BFS y DFS
def imagen():
    global img1, img2, img3
    if len(lista_Vertices) > 0:
        # Grafo original
        plt.figure(figsize=(4, 4))  # Tamaño reducido
        nx.draw(grafo, with_labels=True, node_color='lightblue', font_weight='bold')
        plt.savefig("grafo_original.png")
        img1 = mostrar_imagen("grafo_original.png", 600, 10)  # Esquina superior derecha
        label_original = tk.Label(ventana, text="Grafo Original", font=("Helvetica", 14, 'bold'))
        label_original.place(x=600, y=320)  # Ajusta la posición de la etiqueta

        # BFS
        bfs_tree = list(nx.bfs_edges(grafo, lista_Vertices[0]))
        bfs_graph = nx.DiGraph(bfs_tree)
        plt.figure(figsize=(4, 4))  # Tamaño reducido
        nx.draw(bfs_graph, with_labels=True, node_color='lightgreen', font_weight='bold')
        plt.savefig("bfs_grafo.png")
        img2 = mostrar_imagen("bfs_grafo.png", 50, 350)  # Ajusta la posición de la imagen
        label_bfs = tk.Label(ventana, text="Grafo de búsqueda a lo ancho", font=("Helvetica", 14, 'bold'))
        label_bfs.place(x=50, y=670)  # Ajusta la posición de la etiqueta

        # DFS
        dfs_tree = list(nx.dfs_edges(grafo, lista_Vertices[0]))
        dfs_graph = nx.DiGraph(dfs_tree)
        plt.figure(figsize=(4, 4))  # Tamaño reducido
        nx.draw(dfs_graph, with_labels=True, node_color='lightcoral', font_weight='bold')
        plt.savefig("dfs_grafo.png")
        img3 = mostrar_imagen("dfs_grafo.png", 600, 350)  # Ajusta la posición de la imagen
        label_dfs = tk.Label(ventana, text="Grafo de búsqueda a lo largo", font=("Helvetica", 14, 'bold'))
        label_dfs.place(x=600, y=670)  # Ajusta la posición de la etiqueta
    else:
        mensaje("No hay grafo para mostrar")

# Función para mostrar imágenes
def mostrar_imagen(filepath, x, y):
    img = Image.open(filepath)
    img = img.resize((300, 300), Image.LANCZOS)  # Tamaño reducido
    render = ImageTk.PhotoImage(img)
    label = Label(ventana, image=render)
    label.image = render
    label.place(x=x, y=y)
    return label

# Actualizar la lista de vértices
def recorrer_listaVertices():
    for widget in lista_labels:  # Limpiar etiquetas anteriores
        widget.destroy()
    lista_labels.clear()
    
    for numero, vertice in enumerate(lista_Vertices):
        nombre_label = tk.Label(ventana, text=f"{vertice}", font=("Helvetica", 12))  # Aumentar tamaño de fuente
        nombre_label.grid(row=numero, column=0, sticky='w', padx=10, pady=2)
        lista_labels.append(nombre_label)  # Agregar etiqueta a la lista para limpieza

# Mensaje de Error
def mensaje(infoM):
    messagebox.showerror("Error", infoM)

# Obtener los datos del vértice
def on_button_click():
    nombreVertice = txt_vertice.get()
    crear_vertice(nombreVertice)

# Ingresar los datos para la arista
def on_button_click2():
    vertices = txt_arista.get().split(',')
    if len(vertices) == 2:
        crear_arista(vertices[0].strip(), vertices[1].strip())
    else:
        mensaje("Debe ingresar dos vértices separados por coma")

# Creación de un input para el vértice
txt_vertice = tk.Entry(ventana, width=25)
txt_vertice.grid(row=3, column=2, padx=10, pady=10)

# Botón para agregar vértice
boton_vertice = tk.Button(ventana, text="Agregar Vértice", command=on_button_click)
boton_vertice.grid(row=3, column=1, padx=10, pady=10)

# Creación de un input para la arista
txt_arista = tk.Entry(ventana, width=25)
txt_arista.grid(row=4, column=2, padx=10, pady=10)

# Botón para agregar arista
boton_arista = tk.Button(ventana, text="Agregar Arista", command=on_button_click2)
boton_arista.grid(row=4, column=1, padx=10, pady=10)

# Botón para mostrar el grafo y las búsquedas
boton_grafo = tk.Button(ventana, text="Mostrar El Grafo", command=imagen)
boton_grafo.grid(row=5, column=1, padx=10, pady=50)

# Lista para almacenar las etiquetas
lista_labels = []

ventana.mainloop()

