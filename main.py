import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from data_viewer import XMLViewerApp
from json_viewer import JsonViewerApp
from xsl_viewer import XSLViewerApp
from name_viewer import NameViewerApp
import xml.etree.ElementTree as ET
import json

class HomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Evidenta pacientilor ce urmeaza anumite tratamente")
        self.minsize(1000, 700)
        self.style = ttk.Style()
        self.tk.call('lappend', 'auto_path', 'themes')

        # Centrare fereastra
        self.center_window(1000, 700)

        # Titlu
        title_label = tk.Label(self, text="Evidenta pacientilor ce urmeaza anumite tratamente", font=("Arial", 24))
        title_label.pack(pady=20)

        # Imagine logo
        self.image = Image.open("logo.png")  # Incarca imaginea
        self.image = self.image.resize((626, 306), Image.LANCZOS)  # Redimensionare
        self.img = ImageTk.PhotoImage(self.image)
        image_label = tk.Label(self, image=self.img)
        image_label.pack(pady=20)

        # Butoane
        view_data_btn = tk.Button(self, text="Vizualizare Pacienti (Parsare XML)", command=self.open_viewer)
        view_data_btn.pack(pady=10)

        view_json_btn = tk.Button(self, text="Vizualizare Pacienti (Parsare JSON)", command=self.open_json_viewer)
        view_json_btn.pack(pady=10)

        view_xsl_btn = tk.Button(self, text="Vizualizare ca XSL", command=self.open_xsl_viewer)
        view_xsl_btn.pack(pady=10)

        # Eticheta si caseta text pentru cautare
        search_label = tk.Label(self, text="Cauta dupa nume:")
        search_label.pack(pady=5)

        self.search_entry = tk.Entry(self)
        self.search_entry.pack(pady=5)

        # Buton de cautare
        search_button = tk.Button(self, text="Cautare", command=self.open_viewer_with_search_query)
        search_button.pack(pady=5)


    def center_window(self, width, height):
        # Obtine dimensiunile ecranului
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculeaza pozitia x si y pentru fereastra centralizata
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Seteaza pozitia ferestrei
        self.geometry(f'{width}x{height}+{x}+{y}')

    def open_viewer(self):
        # Ascunde fereastra principala
        self.withdraw()
        # Creaza o noua fereastra secundara
        viewer_window = tk.Toplevel(self)
        # Initializeaza PacientViewerApp cu fereastra noua
        XMLViewerApp(viewer_window)
        # Seteaza un handler pentru atunci cand fereastra secundara este inchisa
        viewer_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close_viewer(viewer_window))

    def on_close_viewer(self, viewer_window):
        # Aceasta functie va fi apelata atunci cand fereastra secundara este inchisa
        viewer_window.destroy()  # Distrugerea ferestrei secundare
        self.deiconify()  # Reafisarea ferestrei principale

    def open_json_viewer(self):
        self.withdraw()  # Ascunde fereastra principala
        json_window = JsonViewerApp(self)  # Initializeaza DataAdderApp cu fereastra noua
        json_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close_json_viewer(json_window))  # Gestionarea inchiderii ferestrei

    def on_close_json_viewer(self, json_window):
        json_window.destroy()  # Distruge fereastra secundara
        self.deiconify()  # Reafiseaza fereastra principala

    def open_xsl_viewer(self):
        # Ascunde fereastra principala
        self.withdraw()
        # Creaza o noua fereastra secundara
        xsl_viewer_window = XSLViewerApp()
        # Seteaza un handler pentru atunci cand fereastra secundara este inchisa
        xsl_viewer_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close_xsl_viewer(xsl_viewer_window))

    def on_close_xsl_viewer(self, xsl_viewer_window):
        # Aceasta functie va fi apelata atunci cand fereastra secundara este inchisa
        xsl_viewer_window.destroy()  # Distrugerea ferestrei secundare
        self.deiconify()  # Reafisarea ferestrei principale

    def open_viewer_with_search_query(self):
        search_query = self.search_entry.get()  # Obtine textul introdus in caseta text
        self.withdraw()
        # Deschide fereastra de vizualizare XML si transmite numele cautat
        name_viewer_window = tk.Toplevel(self)
        NameViewerApp(name_viewer_window, search_query)
        name_viewer_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close_viewer(name_viewer_window))

    def hide(self):
        # Ascunde fereastra
        self.withdraw()

    def show(self):
        # Redeschide fereastra principala
        self.update()
        self.deiconify()

if __name__ == "__main__":
    app = HomeScreen()
    app.mainloop()
