import tkinter as tk
import os

class CreatePasswordWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Crear Nueva Contraseña")
        self.root.geometry("800x600")
        self.root.configure(bg="black")  # Fondo negro
        self.root.resizable(False, False)  # No redimensionable

        # Estilo de borde para los contenedores
        border_style = {"borderwidth": 2, "relief": "solid"}

        # Contenedor principal para los inputs
        input_container = tk.Frame(self.root, bg="white", padx=20, pady=10, **border_style)
        input_container.pack(padx=20, pady=20)

        # Input para correo electrónico
        tk.Label(input_container, text="Correo Electrónico:", font=("Helvetica", 12, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=10)
        self.email_entry = tk.Entry(input_container, font=("Helvetica", 12), width=40)
        self.email_entry.grid(row=0, column=1, pady=10)

        # Input para plataforma
        tk.Label(input_container, text="Plataforma:", font=("Helvetica", 12, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=10)
        self.platform_entry = tk.Entry(input_container, font=("Helvetica", 12), width=40)
        self.platform_entry.grid(row=1, column=1, pady=10)

        # Input para nombre de usuario
        tk.Label(input_container, text="Nombre de Usuario:", font=("Helvetica", 12, "bold"), bg="white").grid(row=2, column=0, sticky="w", pady=10)
        self.username_entry = tk.Entry(input_container, font=("Helvetica", 12), width=40)
        self.username_entry.grid(row=2, column=1, pady=10)

        # Input para contraseña
        tk.Label(input_container, text="Contraseña:", font=("Helvetica", 12, "bold"), bg="white").grid(row=3, column=0, sticky="w", pady=10)
        self.password_entry = tk.Entry(input_container, font=("Helvetica", 12), width=40, show="*")
        self.password_entry.grid(row=3, column=1, pady=10)

        # Botón para mostrar/ocultar la contraseña
        self.show_password = False
        self.toggle_button = tk.Button(input_container, text="👁", command=self.toggle_password, bg="#FFD700", relief="flat")
        self.toggle_button.grid(row=3, column=2, padx=10)

        # Contenedor para los botones
        button_container = tk.Frame(self.root, bg="white", padx=20, pady=10, **border_style)
        button_container.pack(padx=20, pady=20)

        # Botón Cancelar
        cancel_button = tk.Button(button_container, text="Cancelar", bg="#00BFFF", fg="white", font=("Helvetica", 12, "bold"), command=self.cancel)
        cancel_button.pack(side=tk.LEFT, padx=10, ipadx=10)

        # Botón Agregar Contraseña
        add_button = tk.Button(button_container, text="Agregar Contraseña", bg="#00BFFF", fg="white", font=("Helvetica", 12, "bold"), command=self.add_password)
        add_button.pack(side=tk.RIGHT, padx=10, ipadx=10)

    def toggle_password(self):
        if self.show_password:
            self.password_entry.config(show="*")
            self.toggle_button.config(text="👁")
        else:
            self.password_entry.config(show="")
            self.toggle_button.config(text="👁‍🗨")
        self.show_password = not self.show_password

    def cancel(self):
        self.root.destroy()

    def add_password(self):
        # Aquí puedes agregar la lógica para manejar la creación de una nueva contraseña
        email = self.email_entry.get()
        platform = self.platform_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Por ejemplo, mostrar un mensaje de confirmación
        tk.messagebox.showinfo("Información", f"Contraseña para {platform} agregada exitosamente.")
        # Limpiar los campos de entrada después de agregar la contraseña
        self.email_entry.delete(0, tk.END)
        self.platform_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CreatePasswordWindow(root)
    root.mainloop()
