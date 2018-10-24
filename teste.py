# -*- coding: utf-8 -*-

from tkinter import *
import unicodedata
import tkinter.scrolledtext as tkscrolled
class ManipulaTexto(object):

    def __init__(self, instancia):




        # caixa de texto 1
        self.tx = tkscrolled.ScrolledText(instancia, width=400, height=15, undo=True)

        self.tx.insert(END, "\n".join(["     marcelo moreira", "kiara fafa", "", "eu tu", ""]))


        # caixa de texto 2
        self.tx2 = tkscrolled.ScrolledText(instancia, width=400, height=15, undo=True)

        self.texto = Entry(instancia)



        self.bt = Button(instancia, width=20, text="ok", command=self.manipula)
        self.bt1 = Button(instancia, width=20, text="Tratar nome", command=self.manipula)
        self.bt2 = Button(instancia, width=20, text="Tratar telefone", command=self.manipula)

        self._cb_maiusculo = False
        self._check_button_maiusculo = Checkbutton(instancia, text = "Converter para maiusculo", command=self.click_maiusculo)

        self._cb_acentuacao = False
        self._check_button_acentuacao = Checkbutton(instancia, text = "Remover acentuação", command=self.click_acentuacao )

        self.tx.pack(expand=True, fill='both')
        self.tx2.pack(expand=True, fill='both')
        self.bt.pack(side=TOP)
        self._check_button_maiusculo.pack(side=LEFT)
        self._check_button_acentuacao.pack(side=LEFT)
        self.texto.pack(side=LEFT)
        self.bt1.pack(side=LEFT)
        self.bt2.pack(side=LEFT)


    def _remove_acentuacao(self, palavra):
        nfkd = unicodedata.normalize('NFKD', palavra)
        return u"".join([c for c in nfkd if not unicodedata.combining(c)])

    def manipula(self):
        linhas = self.tx.get(1.0, END).split("\n")

        nomes = []

        for nome in linhas[:-1]:
            nome_partes = nome.split()

            if len(nome_partes) > 0:

                primeira_parte = nome_partes[0]

                # tratamento do texto tudo para maiusculo
                if self._cb_maiusculo:
                    primeira_parte = primeira_parte.upper()

                # tratamento para remover acentuacao do texto
                if self._cb_acentuacao:
                    primeira_parte = self._remove_acentuacao(primeira_parte)

                nomes.append(primeira_parte)
            else:
                nomes.append("")

        self.tx2.insert(END, "\n".join(nomes))

    def click_maiusculo(self):
        """define se sera convertido para muiusculo"""
        self._cb_maiusculo = not self._cb_maiusculo

    def click_acentuacao(self):

        self._cb_acentuacao = not self._cb_acentuacao






janela = Tk()
ManipulaTexto(instancia=janela)






janela.geometry("1000x800+200+200")
janela.mainloop()