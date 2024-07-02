# main.py
from tkinter import Tk, Button
from gui.main_window import MainWindow  # Importar MainWindow, no PasswordManagerWindow

class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Mi Proyecto")
        self.geometry("800x600")
        self.configure(bg="black")  # Establecer fondo negro
        self.resizable(False, False)  # Evitar redimensionamiento de la ventana

        # Configurar el botón con las propiedades solicitadas
        button = Button(self, text="Ingresar a gestor de contraseñas", 
                        bg="#00BFFF", fg="white", 
                        font=("Helvetica", 16), 
                        width=25, height=2, 
                        command=self.open_password_manager)
        button.pack(pady=(100, 10))  # margen superior de 100 píxeles, margen inferior de 10 píxeles

    def open_password_manager(self):
        self.destroy()  # Cerrar la ventana principal
        password_manager = MainWindow()  # Crear instancia de MainWindow
        password_manager.mainloop()  # Abrir la ventana del gestor de contraseñas

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
