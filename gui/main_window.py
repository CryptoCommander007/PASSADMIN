# gui/main_window.py
import tkinter as tk
import subprocess  # Para abrir los archivos .py externos
import os

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Contraseñas")
        self.geometry("800x600")
        self.configure(bg="black")  # Fondo negro
        self.resizable(False, False)  # No redimensionable

        # Botones adicionales
        btn_consultar = tk.Button(self, text="Consultar contraseñas", 
                                  bg="#00BFFF", fg="white", 
                                  font=("Helvetica", 14), 
                                  width=20, height=2, 
                                  command=self.consultar_passwords)
        btn_consultar.pack(pady=50)

        btn_crear = tk.Button(self, text="Crear contraseña", 
                              bg="#00BFFF", fg="white", 
                              font=("Helvetica", 14), 
                              width=20, height=2, 
                              command=self.crear_password)
        btn_crear.pack(pady=50)

        btn_modificar = tk.Button(self, text="Modificar contraseña", 
                                  bg="#00BFFF", fg="white", 
                                  font=("Helvetica", 14), 
                                  width=20, height=2, 
                                  command=self.modificar_password)
        btn_modificar.pack(pady=50)

    def consultar_passwords(self):
        script_path = os.path.join(os.path.dirname(__file__), "get_password.py")
        subprocess.Popen(["python", script_path])

    def crear_password(self):
        script_path = os.path.join(os.path.dirname(__file__), "create_password.py")
        subprocess.Popen(["python", script_path])

    def modificar_password(self):
        script_path = os.path.join(os.path.dirname(__file__), "modify_password.py")
        subprocess.Popen(["python", script_path])

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
