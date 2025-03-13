import tkinter as tk
from tkinter import ttk
import xml.etree.ElementTree as ET

def parse_xml():
    # Parsare XML
    tree = ET.parse("evidenta_pacienti.xml")
    root = tree.getroot()

    # Defineste structura de date pentru a pastra toate datele
    data = []

    # Iteratie la pacienti
    for pacient_elem in root.findall('pacient'):
        pacient_info = {
            'ID': pacient_elem.get('id'),
            'Nume': pacient_elem.find('nume').text,
            'Varsta': pacient_elem.find('varsta').text,
            'Tratament': {}
        }

        # Iteratie la tratamente
        for tratament_elem in pacient_elem.findall('tratament'):
            tratament_info = {
                'Denumire': tratament_elem.find('denumire').text,
                'Doza': tratament_elem.find('doza').text,
                'Frecventa': tratament_elem.find('frecventa').text
            }
            pacient_info['Tratament'] = tratament_info
            data.append(pacient_info.copy())

    return data


def open_detail_window(title, columns, data):
    detail_window = tk.Toplevel()
    detail_window.title(title)
    detail_window.minsize(1200, 300) 
    tree = ttk.Treeview(detail_window, columns=columns, show='headings')
    tree.pack(fill=tk.BOTH, expand=True)
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    for row_data in data:
        tree.insert('', 'end', values=row_data)


class XMLViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Evidenta Pacienti")
        self.root.minsize(1200, 600)
        self.parsed_data = parse_xml()
        self.setup_tree()

    def setup_tree(self):
        self.tree_view = ttk.Treeview(self.root)
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.tree_view['columns'] = ("ID", "Nume", "Varsta", "Denumire Tratament", "Doza Tratament", "Frecventa Tratament")
        for col in self.tree_view['columns']:
            self.tree_view.heading(col, text=col)
            self.tree_view.column(col, width=150)  
        self.tree_view["show"] = "headings"
        self.populate_tree()

    def populate_tree(self):
        for pacient in self.parsed_data:
            self.tree_view.insert('', 'end', values=(
                pacient['ID'],
                pacient['Nume'],
                pacient['Varsta'],
                pacient['Tratament']['Denumire'],
                pacient['Tratament']['Doza'],
                pacient['Tratament']['Frecventa']
            ))

        self.tree_view.bind('<Double-1>', self.on_item_double_click)

    def on_item_double_click(self, event):
        item = self.tree_view.selection()[0]
        col = self.tree_view.identify_column(event.x)
        pacient_index = self.tree_view.index(item)
        pacient_data = self.parsed_data[pacient_index]

        # Determinam pe ce coloana s-a facut dublu-click
        if col in ('#4', '#5', '#6'):  # Tratament
            self.open_tratament_window(pacient_data)

    def open_tratament_window(self, pacient_data):
        tratament_data = [(pacient_data['Tratament']['Denumire'], pacient_data['Tratament']['Doza'], pacient_data['Tratament']['Frecventa'])]
        open_detail_window("Tratament", ['Denumire', 'Doza', 'Frecventa'], tratament_data)


if __name__ == "__main__":
    root = tk.Tk()
    app = XMLViewerApp(root)
    root.mainloop()
