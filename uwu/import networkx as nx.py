import tkinter as tk
from tkinter import ttk
import pandas as pd

def buscar_nombre():
    Name = entry_nombre.get()
    
    if not Name:
        resultado.set("Por favor, ingrese un nombre.")
    else:
        # Cargamos el archivo CSV
        try:
            df = pd.read_csv('anime-dataset-2023.csv')
            resultado.set(df[df['Name'] == Name])
        except FileNotFoundError:
            resultado.set("El archivo CSV no se encontró.")

# Crear la ventana principal
root = tk.Tk()
root.title("Búsqueda en CSV")

# Establecer la imagen de fondo
background_image = tk.PhotoImage(file="fotouwu.png")  # Reemplaza con la ruta de tu imagen
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Establece el tamaño para que la imagen cubra toda la ventana

# Crear etiqueta y entrada para el nombre
etiqueta_nombre = ttk.Label(root, text="Name:")
etiqueta_nombre.pack()
entry_nombre = ttk.Entry(root)
entry_nombre.pack()

# Botón para buscar
boton_buscar = ttk.Button(root, text="Buscar", command=buscar_nombre)
boton_buscar.pack()

# Resultado de la búsqueda
resultado = tk.StringVar()
etiqueta_resultado = ttk.Label(root, textvariable=resultado)
etiqueta_resultado.pack()

root.mainloop()
