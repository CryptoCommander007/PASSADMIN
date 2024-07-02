import tkinter as tk
import os

class GetPasswordWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana de Contraseñas")
        self.root.geometry("800x600")
        self.root.configure(bg="black")  # Fondo negro
        self.root.resizable(False, False)  # No redimensionable

        # Estilo de borde para los contenedores
        border_style = {"borderwidth": 2, "relief": "solid"}

        # Crear la cuadrícula para organizar los elementos
        for i in range(3):
            # Contenedor para cada fila de la "tabla"
            container = tk.Frame(self.root, bg="white", padx=20, pady=10, **border_style)
            container.grid(row=i, column=0, padx=10, pady=10, sticky="nsew")

            # Cargar imagen
            img_path = os.path.join(os.path.dirname(__file__), "..", "resources", "images", "icon_user.jpg")
            try:
                img = tk.PhotoImage(file=img_path).subsample(3)  # Ajusta tamaño de la imagen
                label_img = tk.Label(container, image=img)
                label_img.grid(row=i, column=0, padx=10, pady=10)

            except tk.TclError as e:
                print(f"No se pudo cargar la imagen: {e}")

            # Correo electrónico
            email = f"correo{i+1}@gmail.com"
            label_email = tk.Label(container, text=email, font=("Helvetica", 12, "bold"), fg="black")
            label_email.grid(row=i, column=1, padx=10, pady=10)

            # Contraseña (solo visual)
            password = ["531d%%jMhjfjrn46QQ", "%jfdhen%6Mgjdh%3W", "3%jfd46gjdGh%$341A"][i]
            label_password = tk.Label(container, text=password, font=("Helvetica", 10), fg="black")
            label_password.grid(row=i, column=2, padx=10, pady=10)

            # Detalles (por ejemplo)
            details = tk.Button(container, text="Detalles", bg="#00BFFF", fg="white", font=("Helvetica", 10), width=10)
            details.grid(row=i, column=3, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = GetPasswordWindow(root)
    root.mainloop()
