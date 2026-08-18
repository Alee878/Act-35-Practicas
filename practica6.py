import tkinter as tk
ventana=tk.Tk() #Crea la ventana

ventana.title("Mi ventana")#Cambiar titulo
ventana.geometry("1100x550")#definir el tamaño

boton=tk.Button(ventana, text="Press here")
boton.pack(pady=20)

ventana.mainloop()#mantener la ventana abierta