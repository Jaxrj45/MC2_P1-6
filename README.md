### Manual de Usuario

#### 1. Descripción General

Este programa permite la creación y visualización de grafos interactivos mediante una 
interfaz gráfica sencilla utilizando Tkinter y Graphviz. Los usuarios pueden agregar 
vértices y aristas, y visualizar el grafo resultante en un formato de imagen.

#### 2. Requisitos del Sistema

1. Python 3.x instalado. 
2. *Instalación de las siguientes librerías*:
   - Tkinter (generalmente incluida en Python). 
   - Graphviz. 
   - Pillow para manejar las imágenes.
   Para instalar las dependencias, utiliza:
   - `pip install graphviz pillow`
   - Además, deberás instalar Graphviz en tu sistema y asegurarte de que está configurado en tu PATH. Puedes descargarlo desde [Graphviz.org.](https://graphviz.org)

#### 3. Instalación 

1. Descarga o clona el código desde el repositorio.
2. Asegúrate de tener instaladas todas las dependencias mencionadas. 
3. Ejecuta el archivo Python proyecto.py.

### 4. Interfaz de Usuario

La interfaz está diseñada para ser fácil de usar y consta de las siguientes secciones:
- *Área de Imagen*: Muestra el grafo generado por el usuario.
- *Área de botones*: Se realiza el ingreso de vértices y aristas, también se genera el grafo y los árboles de búsqueda.

![alt text](image-1.jpg)

#### 5. Uso del Programa

1. *Iniciar el programa*:Abre el programa y espera a que se cargue la interfaz principal.En la parte izquierda de la ventana, verás dos campos de entrada, uno para los vértices y otro para las aristas, junto con un botón para generar el grafo.
   
2. *Ingresar Vértices*:En el campo Vértice, escribe el nombre o valor del vértice que deseas agregar. Presiona Enter o el botón de agregar (si está disponible) para registrar el vértice en el programa. El vértice ingresado se agregará a la lista de vértices mostrada en la sección de resumen a la derecha.

3. *Ingresar Aristas*: En el campo Arista, ingresa la conexión entre dos vértices en el formato A,B, donde A es el vértice de origen y B es el vértice de destino.
Presiona Enter o el botón de agregar arista para registrar la arista en el programa. La arista ingresada aparecerá en el resumen a la derecha junto con el resto de vértices y aristas ingresados.
![alt text](image-2.jpg)

4. *Mostrar el Grafo*: Una vez que hayas ingresado todos los vértices y aristas necesarios, haz clic en el botón Mostrar el Grafo. El grafo original se mostrará en  la pantalla, mostrando los vértices y las conexiones tal como las ingresaste.


5. *Aplicar el Algortimo de busqueda de anchura o largo*:
   En el lado izquierdo abajo de la pantalla, se generará el grafo con el algoritmo de búsqueda en anchura o largo aplicado. Este grafo destacará el orden de los nodos explorados según el algoritmo. Los resultados visuales permitirán comparar el grafo original y el grafo procesado con la búsqueda en anchura.
