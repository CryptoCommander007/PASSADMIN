import tkinter as tk
class Widget2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Soy el Widget 2")
        label.pack()
