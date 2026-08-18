import tkinter as tk

def mostrar_saludo():
    nombre=caja_nombre.get()
    mensaje.config(text="Bienvenido, "+nombre+ "!") 

ventana=tk.Tk()
ventana.title("Ingreso de nombre")
ventana.geometry("600x450")

tk.Label(
    ventana,
    text="Ingrese su nombre",
    font=("Arial", 12)
).pack(pady=10)

caja_nombre=tk.Entry(
    ventana,
    width=30
)
caja_nombre.pack()

boton=tk.Button(
    ventana,
    text="Mostrar saludo",
    command=mostrar_saludo
)
boton.pack(pady=20)

mensaje=tk.Label(
    ventana,
    text="",
    font=("Arial", 12),
    fg="blue"
)
mensaje.pack()

ventana.mainloop

