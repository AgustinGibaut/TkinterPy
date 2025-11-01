#TKINTER (IMPORTADO)
import tkinter as tk
#MODULO TTK (es una mejora de la libreria de tkinder.)
from tkinter import ttk

#CONFIGURACION INICIAL
ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("REPRODUCTOR MUSICAL")

#CREAMOS ETIQUETA
etiqueta = tk.Label(ventana, text="HOLA, ACA SE MUESTRA EL TEXTO")

#PUBLICAMOS EL COMPONENTES
etiqueta.pack(pady=50)

#tambien se puede cambiar el texto usando configure
etiqueta.configure(text="Texto Modificado...")

#Tambien, se pude modificar el texto con la ayuda de la llave Text
etiqueta["text"] = "TAEXTO QUE SE PASO A MAYUSCULAS"

#IMPORTANTE PARA PODER EJECUTAR LA VENTANA DE LA APLICACION.
ventana.mainloop()