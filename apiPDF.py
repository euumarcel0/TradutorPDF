import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import fitz 
from googletrans import Translator

class Tradutor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tradução")

        self.label = tk.Label(self.root, text="Digite o caminho do PDF:")
        self.label.pack()

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Traduzir", command=self.leitura)
        self.button.pack()

        self.progress = Progressbar(self.root, orient="horizontal", length=200, mode="determinate")
        self.progress.pack()

        self.label_progress = tk.Label(self.root, text="")
        self.label_progress.pack()

        self.root.mainloop()

    def leitura(self):
        try:
            caminho_pdf = self.entry.get()
            documento_pdf = fitz.open(caminho_pdf)
            total_paginas = documento_pdf.page_count
            novo_pdf = fitz.open()

            for pagina_num in range(total_paginas):
                pagina = documento_pdf[pagina_num]
                text = pagina.get_text("text")
                if text is not None:
                    texto_traduzido = self.traduzir_texto(text, 'pt')
                    if texto_traduzido is not None:
                        self.adicionar_pagina_pdf(novo_pdf, texto_traduzido)
                progresso = ((pagina_num + 1) / total_paginas) * 100
                self.progress['value'] = progresso
                self.label_progress.config(text=f"Tradução: {int(progresso)}%")
                self.root.update_idletasks()

            caminho_saida = "output_traduzido.pdf"
            novo_pdf.save(caminho_saida)
            novo_pdf.close()
            print(f"Novo PDF criado em: {caminho_saida}")

        except Exception as e:
            print(f"Erro: {e}")

    def traduzir_texto(self, texto, destino='pt'):
        translator = Translator()
        traducao = translator.translate(texto, dest=destino)
        print(f"Texto Traduzido:\n{traducao.text}")
        return traducao.text

    def adicionar_pagina_pdf(self, pdf_writer, texto):
        nova_pagina = pdf_writer.new_page(width=600, height=800)
        nova_pagina.insert_text((10, 10), texto)

if __name__ == "__main__":
    tradutor = Tradutor()
