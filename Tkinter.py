#IMPORTAR TKINTER.
import tkinter as tk

#AHORA CREAR LA INTERFAZ DE TKINTER.
ventana = tk.Tk()

#REDIMENCIONAR LA VENTANA.
ventana.geometry("600x400")

#MODIFICAR EL TITULO DE LA VENTANA.
ventana.title("REPRODUCTOR MUSICAL")

#EVITAR REDIMENSIONAR LA VENTANA
ventana.resizable(0,0)

#HACER VISIBLE LA VENTANA.
ventana.mainloop()

#MODIFICAR EL COLOR DE LA VENTANA
ventana.configure(background="#fffffff")