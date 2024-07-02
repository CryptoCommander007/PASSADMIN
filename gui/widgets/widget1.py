import tkinter as tk
class Widget1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Soy el Widget 1")
        label.pack()
