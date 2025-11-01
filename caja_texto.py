import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x800")
ventana.title("Nueva Ventana")
ventana.configure(background="yellow")

etiqueta = tk.Label(ventana, text="Esto sería un texto que se muestra en pantalla.")
etiqueta.pack(pady=50)

def mostrar():
    text = caja_texto.get()
    print(f"Texto proporcionado: {text}")

caja_texto = ttk.Entry(ventana, font=("Arial", 15))
caja_texto.pack(padx=20)

button = ttk.Button(ventana, text="Enviar", command=mostrar)
button.pack(pady=20)

ventana.mainloop()
