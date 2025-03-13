import tkinter as tk
from tkinter import ttk
import json

def parse_json():
    with open("evidenta_pacienti.json") as json_file:
        data = json.load(json_file)
        return data["evidenta_pacienti"]["pacient"]

class JsonViewerApp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Vizualizare Pacienti din JSON")
        self.geometry("800x400")
        self.json_data = parse_json()
        self.create_tree()

    def create_tree(self):
        self.tree_view = ttk.Treeview(self, show="headings")
        self.tree_view['columns'] = ("ID", "Nume", "Varsta", "Tratament")
        for col in self.tree_view['columns']:
            self.tree_view.heading(col, text=col)
            self.tree_view.column(col, width=150)
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.display_json_data()

    def display_json_data(self):
        for pacient in self.json_data:
            pacient_id = pacient.get('@id', 'N/A')
            nume = pacient.get('nume', 'N/A')
            varsta = pacient.get('varsta', 'N/A')
            tratamente = ""
            if isinstance(pacient['tratament'], list):
                for tratament in pacient['tratament']:
                    denumire = tratament.get('denumire', 'N/A')
                    doza = tratament.get('doza', 'N/A')
                    frecventa = tratament.get('frecventa', 'N/A')
                    tratamente += f"{denumire}: {doza}, frecventa: {frecventa}\n"
            else:
                denumire = pacient['tratament'].get('denumire', 'N/A')
                doza = pacient['tratament'].get('doza', 'N/A')
                frecventa = pacient['tratament'].get('frecventa', 'N/A')
                tratamente = f"{denumire}: {doza}, frecventa: {frecventa}"
            self.tree_view.insert('', 'end', values=(pacient_id, nume, varsta, tratamente))


if __name__ == "__main__":
    root = tk.Tk()
    app = JsonViewerApp(root)
    root.mainloop()
