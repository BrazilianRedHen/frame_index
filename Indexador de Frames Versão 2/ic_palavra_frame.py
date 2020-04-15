from tkinter import *
import random
import sys

frameelements = [
                {"frame": "Scrutiny",
                    "iten1": "analyse",
                    "iten2": "analysis",
                    "iten3": "analyst",
                    "iten4": "analytic",
                    "tipoiten1": "v",
                    "tipoiten2": "n",
                    "tipoiten3": "n",
                    "tipoiten4": "a"
                },

                {"frame": "Cardinal Numbers",
                    "iten1": "brace",
                    "iten2": "couple",
                    "iten3": "dual",
                    "iten4": "fourteen",
                    "tipoiten1": "n",
                    "tipoiten2": "n",
                    "tipoiten3": "a",
                    "tipoiten4": "n"
                },

                {"frame": "Means",
                    "iten1": "approach",
                    "iten2": "means",
                    "iten3": "mechanism",
                    "iten4": "method",
                    "tipoiten1": "n",
                    "tipoiten2": "n",
                    "tipoiten3": "n",
                    "tipoiten4": "n"

                }
                ]
itens_lexais = ["analyse","analysis","analyst","analytic",
                "brace", "couple", "dual","fourteen",
                "approach", "means", "mechanism","method"
]

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 20
        self.sextoContainer.pack()

        self.setimoContainer = Frame(master)
        self.setimoContainer["pady"] = 20
        self.setimoContainer.pack()

        self.oitavoContainer = Frame(master)
        self.oitavoContainer["pady"] = 20
        self.oitavoContainer.pack()

        self.nonoContainer = Frame(master)
        self.nonoContainer["pady"] = 20
        self.nonoContainer.pack()

        self.decimoContainer = Frame(master)
        self.decimoContainer["pady"] = 20
        self.decimoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Indexador de Frames - Versão 2")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.frameLabel = Label(self.segundoContainer, text="Qual frame é evocado pelo seguinte ítem lexical: ", font=self.fontePadrao)
        self.frameLabel.pack(side=LEFT)

        self.itemLexical = random.choice(itens_lexais)

        self.iten1Label = Label(self.terceiroContainer, text="%s: "%self.itemLexical, font=self.fontePadrao)
        self.iten1Label.pack(side=LEFT)
        self.iten1 = Entry(self.terceiroContainer)
        self.iten1["width"] = 30
        self.iten1["font"] = self.fontePadrao
        self.iten1.pack(side=LEFT)

        self.verificar = Button(self.quartoContainer)
        self.verificar["text"] = "Verificar"
        self.verificar["font"] = ("Calibri", "8")
        self.verificar["width"] = 12
        self.verificar["command"] = self.verificaTipo
        self.verificar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.sair = Button(self.quintoContainer)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 12
        self.sair["command"] = self.exit
        self.sair.pack_forget()

    def verificaTipo(self):
        self.verificar.pack_forget()
        self.sair.pack()
        self.itemLexical
        i1 = self.iten1.get()
        contador = 0
        for frameelement in [a for a in frameelements if a["frame"] == i1]:
            if self.itemLexical == frameelement["iten1"] or self.itemLexical == frameelement["iten2"] or self.itemLexical == frameelement["iten3"] or self.itemLexical == frameelement["iten4"]:
                contador = contador + 1
                self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao, foreground='green')
                self.mensagem.pack()
                self.mensagem["text"] = "Correto! O ítem lexial %s evoca o frame %s" % (self.itemLexical, i1)
            else:
                for frameCorreto in frameelements:
                    if self.itemLexical == frameCorreto["iten1"] or self.itemLexical == frameCorreto["iten2"] or self.itemLexical == frameCorreto["iten3"] or self.itemLexical == frameCorreto["iten4"]:
                        contador = contador + 1
                        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao, foreground='red')
                        self.mensagem.pack()
                        self.mensagem["text"] = "Errado! O ítem lexial %s evoca o frame %s" % (self.itemLexical, frameCorreto["frame"])

        if contador == 0:
            self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao, foreground='red')
            self.mensagem.pack()
            self.mensagem["text"] = "Errado!"


    def exit(self):
        sys.exit()

root = Tk()
Application(root)
root.mainloop()
