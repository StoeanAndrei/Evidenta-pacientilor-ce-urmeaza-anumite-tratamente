import tkinter as tk
import tkinterweb
import lxml.etree as ET

class XSLViewerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vizualizare XSL")
        self.geometry("1200x600")

        # Frame pentru continut
        content_frame = tk.Frame(self)
        content_frame.pack(expand=True, fill=tk.BOTH)

        # Label pentru titlu
        title_label = tk.Label(content_frame, text="Vizualizare XML aplicand XSL", font=("Helvetica", 16))
        title_label.pack(pady=20)

        # Buton pentru transformare si afisare
        self.transform_button = tk.Button(content_frame, text="Transforma si Afiseaza", command=self.transform_and_display)
        self.transform_button.pack(pady=10)

        # Creeaza un WebFrame pentru afisarea continutului HTML
        self.web_frame = tkinterweb.HtmlFrame(content_frame, messages_enabled=False)
        self.web_frame.pack(expand=True, fill=tk.BOTH)

    def transform_and_display(self):
        xml_file_path = "evidenta_pacienti.xml"
        xsl_file_path = "evidenta_pacienti.xsl"

        try:
            # Parseaza fisierele XML si XSL
            dom = ET.parse(xml_file_path)
            xslt = ET.parse(xsl_file_path)
            transform = ET.XSLT(xslt)
            newdom = transform(dom)

            # Converteste XML-ul transformt in string HTML
            html_output = ET.tostring(newdom, pretty_print=True, method="html").decode()

            # Actualizeaza WebFrame cu continutul HTML
            self.web_frame.load_html(html_output)

        except ET.XMLSyntaxError as e:
            self.web_frame.load_html(f"<p>Eroare în fișierul XML sau XSL: {e}</p>")
        except Exception as e:
            self.web_frame.load_html(f"<p>A apărut o eroare la procesarea transformării: {e}</p>")

if __name__ == "__main__":
    app = XSLViewerApp()
    app.mainloop()
