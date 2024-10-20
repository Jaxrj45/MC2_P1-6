import tkinter as tk
from graphviz import Digraph, Graph
from graphviz.backend.dot_command import command

dot= Graph(comment='Ejemplo Grafo')


#Lista de Vertices

lista_Vertices=[]
lista_Aristas=[]

#Crear Vertices

def crear_vertice(nombreVertice):

    if nombreVertice=="":
        print("Necesita agregar el nombre del vertice")

    else:
        if nombreVertice in lista_Vertices:
            print('No se puede usar la misma letra')
        else:
           # dot.node(nombreVertice.upper(),nombreVertice.upper())
            lista_Vertices.append(nombreVertice)


#Crear Aristas
def crear_arista(vertice1,vertice2):
    if vertice1 and vertice2 in lista_Vertices:
        aristaNueva = vertice1 + vertice2
        if aristaNueva not in lista_Aristas:
            lista_Aristas.append(aristaNueva)
            dot.edge(f'{vertice1.upper()}',f'{vertice2.upper()}')
        else:
            print('Esta Arista ya existe ')

    else:
        print('Los vertices ingresados no Existen')



#Creando Ventana
ventana = tk.Tk()
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ancho_ventana = 600  # Ancho deseado
alto_ventana = 600  # Alto deseado

# Posicion de la ventana
pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
pos_y = (alto_pantalla // 2) - (alto_ventana // 2)
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

#Funciones
def on_button_click():
    textoVertice = txt_vertice.get()
    crear_vertice(textoVertice)


def on_button_click2():
    textoArista = txt_arista.get().split('-')
    if len(textoArista)<2:
        print('Debe ingresar dos vertices para crear una arista')
    else:
        v1,v2=textoArista
        print(v1)
        print(v2)
        crear_arista(v1,v2)
#Creacion de un input

#**Vertice
txt_vertice = tk.Entry(ventana,width=25)
txt_vertice.pack(pady=10)

#Boton Vertice
boton_vertice = tk.Button(ventana, text="Agregar Vertice",command=on_button_click)
boton_vertice.pack(pady=10)

#*Arista
#Boton Arista
boton_arista = tk.Button(ventana, text="Ingrese el nombre ",command=on_button_click2)
boton_arista.pack(pady=10)

txt_arista = tk.Entry(ventana,width=25)
txt_arista.pack(pady=10)



ventana.mainloop()
dot.render('grafo', format='png', cleanup=True)
dot.view()