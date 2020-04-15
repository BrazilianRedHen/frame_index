from tkinter import *
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

        self.titulo = Label(self.primeiroContainer, text="Indexador de Frames")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.frameLabel = Label(self.segundoContainer, text="Digite um frame: ", font=self.fontePadrao)
        self.frameLabel.pack(side=LEFT)

        self.frame = Entry(self.segundoContainer)
        self.frame["width"] = 30
        self.frame["font"] = self.fontePadrao
        self.frame.pack(side=LEFT)


        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaFrame
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()



    # Método verificar frame
    def verificaFrame(self):
        self.autenticar.pack_forget()
        framedigitado = self.frame.get()
        self.frame.get()
        contador = 0
        for frameelement in [a for a in frameelements if a["frame"] == framedigitado]:
            if framedigitado == frameelement["frame"]:
                contador = contador + 1
                self.mensagem["text"] = ("O frame %s evoca os seguintes ítens lexicais. \n "
                                         "Para cada um deles informe se é verbo (v), substantivo (n) ou adjetivo (a):" % framedigitado)

                self.iten1Label = Label(self.quintoContainer, text="%s: "%frameelement["iten1"], font=self.fontePadrao)
                self.iten1Label.pack(side=LEFT)
                self.iten1 = Entry(self.quintoContainer)
                self.iten1["width"] = 30
                self.iten1["font"] = self.fontePadrao
                self.iten1.pack(side=LEFT)

                self.iten2Label = Label(self.sextoContainer, text="%s: " % frameelement["iten2"], font=self.fontePadrao)
                self.iten2Label.pack(side=LEFT)
                self.iten2 = Entry(self.sextoContainer)
                self.iten2["width"] = 30
                self.iten2["font"] = self.fontePadrao
                self.iten2.pack(side=LEFT)

                self.iten3Label = Label(self.setimoContainer, text="%s: " % frameelement["iten3"],font=self.fontePadrao)
                self.iten3Label.pack(side=LEFT)
                self.iten3 = Entry(self.setimoContainer)
                self.iten3["width"] = 30
                self.iten3["font"] = self.fontePadrao
                self.iten3.pack(side=LEFT)

                self.iten4Label = Label(self.oitavoContainer, text="%s: " % frameelement["iten4"], font=self.fontePadrao)
                self.iten4Label.pack(side=LEFT)
                self.iten4 = Entry(self.oitavoContainer)
                self.iten4["width"] = 30
                self.iten4["font"] = self.fontePadrao
                self.iten4.pack(side=LEFT)


                self.verificar = Button(self.nonoContainer)
                self.verificar["text"] = "Verificar"
                self.verificar["font"] = ("Calibri", "8")
                self.verificar["width"] = 12
                self.verificar["command"] = self.verificaTipo
                self.verificar.pack()

                self.mensagem = Label(self.nonoContainer, text="", font=self.fontePadrao)
                self.mensagem.pack()

                self.sair = Button(self.decimoContainer)
                self.sair["text"] = "Sair"
                self.sair["font"] = ("Calibri", "8")
                self.sair["width"] = 12
                self.sair["command"] = self.exit
                self.sair.pack_forget()

        if contador == 0:
            self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao, foreground='red')
            self.mensagem.pack()
            self.mensagem["text"] = "O Frame digitado não foi encontrado!"

            self.sair = Button(self.decimoContainer)
            self.sair["text"] = "Sair"
            self.sair["font"] = ("Calibri", "8")
            self.sair["width"] = 12
            self.sair["command"] = self.exit
            self.sair.pack()

    def verificaTipo(self):
        self.verificar.pack_forget()
        self.sair.pack()
        til1 = self.iten1.get()
        til2 = self.iten2.get()
        til3 = self.iten3.get()
        til4 = self.iten4.get()
        frame = self.frame.get()
        cont1 = 0
        cont2 = 0
        cont3 = 0
        cont4 = 0
        for frameelement in [a for a in frameelements if a["frame"] == frame]:
            if frameelement["tipoiten1"] == til1:
                self.mensagem = Label(self.nonoContainer, text="", font=self.fontePadrao, foreground='green')
                self.mensagem.pack()
                self.mensagem["text"] = "Correto! O item lexical %s é um %s"%(frameelement["iten1"], til1)
            if frameelement["tipoiten1"] != til1:
                self.mensagem = Label(self.nonoContainer, text="", font=self.fontePadrao, foreground='red')
                self.mensagem.pack()
                self.mensagem["text"] = "Errado! O item lexial %s não é um %s e sim um %s" % (
                frameelement["iten1"], til1, frameelement["tipoiten1"])
            if frameelement["tipoiten2"] == til2:
                self.mensagem = Label(self.nonoContainer, text="", font=self.fontePadrao, foreground='green')
                self.mensagem.pack()
                self.mensagem["text"] = "Correto! O item lexical %s é um %s"%(frameelement["iten2"], til2)
            if frameelement["tipoiten2"] != til2:
                self.mensagem = Label(self.nonoContainer, text="", font=self.fontePadrao, foreground='red')
                self.mensagem.pack()
                self.mensagem["text"] = "Errado! O item lexical %s não é um %s e sim um %s" % (
                frameelement["iten2"], til2, frameelement["tipoiten2"])
            if frameelement["tipoiten3"] == til3:
                self.mensagem = Label(self.nonoContainer, text="", font=self.fontePadrao, foreground='green')
                self.mensagem.pack()
                self.mensagem["text"] = "Correto! O item lexical %s é um %s"%(frameelement["iten3"], til3)
            if frameelement["tipoiten3"] != til3:
                self.mensagem = Label(self.nonoContainer, text="", font=self.fontePadrao, foreground='red')
                self.mensagem.pack()
                self.mensagem["text"] = "Errado! O item lexical %s não é um %s e sim um %s" % (
                frameelement["iten3"], til3, frameelement["tipoiten3"])
            if frameelement["tipoiten4"] == til4:
                self.mensagem = Label(self.nonoContainer, text="", font=self.fontePadrao, foreground='green')
                self.mensagem.pack()
                self.mensagem["text"] = "Correto! O item lexical %s é um %s"%(frameelement["iten4"], til4)
            if frameelement["tipoiten4"] != til4:
                self.mensagem = Label(self.nonoContainer, text="", font=self.fontePadrao, foreground='red')
                self.mensagem.pack()
                self.mensagem["text"] = "Errado! O item lexical %s não é um %s e sim um %s"%(frameelement["iten4"], til4, frameelement["tipoiten4"])

    def exit(self):
        sys.exit()

root = Tk()
Application(root)
root.mainloop()
