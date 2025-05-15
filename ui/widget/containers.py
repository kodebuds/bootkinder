import tkinter as tk
from tkinter import ttk
from ui.theme import Theme

class Container(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)        
        self.grid(sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        label = ttk.Label(self, text="This is inside the Container")
        label.grid(row=0, column=0, padx=20, pady=20)