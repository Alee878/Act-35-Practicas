import customtkinter as ctk
from tkinter import messagebox

# ===========================================
# CONFIGURACIÓN DE LA VENTANA
# ===========================================
ctk.set_appearance_mode("dark")          # Modo oscuro (puedes cambiar a "light" o "system")
ctk.set_default_color_theme("blue")      # Tema de color (blue, green, dark-blue)

# ===========================================
# DICCIONARIO CON USUARIOS REGISTRADOS
# ===========================================
usuarios = {
    "admin": "12345",
    "profesor": "abc123",
    "estudiante": "2026"
}

# ===========================================
# FUNCIÓN PARA INICIAR SESIÓN
# ===========================================
def iniciar_sesion():
    usuario = txt_usuario.get()
    clave = txt_clave.get()

    if usuario in usuarios and usuarios[usuario] == clave:
        messagebox.showinfo("Acceso", f"Bienvenido {usuario}")
        ventana.destroy()                 # Cierra la ventana de login
        menu_principal(usuario)           # Abre el menú principal
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# ==============================================
# FUNCIÓN PARA ABRIR EL MENÚ PRINCIPAL
# ==============================================
def menu_principal(nombre):
    menu = ctk.CTk()
    menu.title("Sistema")
    menu.geometry("600x400")

    # Etiqueta de bienvenida
    ctk.CTkLabel(
        menu,
        text=f"Bienvenido {nombre}",
        font=("Arial", 24, "bold")
    ).pack(pady=40)

    # Botón Ventas
    ctk.CTkButton(
        menu,
        text="Ventas",
        width=200
    ).pack(pady=10)

    # Botón Inventario
    ctk.CTkButton(
        menu,
        text="Inventario",
        width=200
    ).pack(pady=10)

    # Botón Clientes
    ctk.CTkButton(
        menu,
        text="Clientes",
        width=200
    ).pack(pady=10)

    # Botón Salir
    ctk.CTkButton(
        menu,
        text="Salir",
        width=200,
        command=menu.destroy
    ).pack(pady=20)

    menu.mainloop()

# ========================
# CREACIÓN DE LA VENTANA DE LOGIN
# ========================
ventana = ctk.CTk()
ventana.title("Inicio de Sesión")
ventana.geometry("450x450")
ventana.resizable(False, False)   # Nota: es "resizable" con una sola 's'

# ========================
# TÍTULO
# ========================
ctk.CTkLabel(
    ventana,
    text="INICIAR SESIÓN",
    font=("Arial", 28, "bold")
).pack(pady=30)

# ========================
# CAJA DE USUARIO
# ========================
txt_usuario = ctk.CTkEntry(
    ventana,
    width=250,
    placeholder_text="Usuario"
)
txt_usuario.pack(pady=15)

# ========================
# CAJA CONTRASEÑA
# ========================
txt_clave = ctk.CTkEntry(
    ventana,
    width=250,
    placeholder_text="Contraseña",
    show="*"
)
txt_clave.pack(pady=15)

# ========================
# BOTÓN INGRESAR
# ========================
ctk.CTkButton(
    ventana,
    text="Ingresar",
    width=250,
    command=iniciar_sesion       # ¡Importante! el nombre debe coincidir con la función
).pack(pady=25)

# ==============================
# INFORMACIÓN DE PRUEBA
# ==============================
ctk.CTkLabel(
    ventana,
    text="Usuario: admin\nContraseña: 12345",
    font=("Arial", 12)
).pack(pady=10)

# ==============================
# INICIA EL PROGRAMA
# ==============================
ventana.mainloop()