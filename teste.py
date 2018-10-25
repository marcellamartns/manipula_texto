# -*- coding: utf-8 -*-

from tkinter import *
import unicodedata
import tkinter.scrolledtext as tkscrolled
import re

class ManipulaTexto(object):

    def __init__(self, instancia):

        # caixas de texto de rolagem
        self.tx = tkscrolled.ScrolledText(instancia, width=400, height=15, undo=True)
        self.tx2 = tkscrolled.ScrolledText(instancia, width=400, height=15, undo=True)

        # caixa de texto
        self.caixa_texto = Entry(instancia)

        # botoes
        self.bt1 = Button(instancia, width=20, text="Tratar nome", command=self.tratar_nome)
        self.bt2 = Button(instancia, width=20, text="Tratar telefone", command=self.tratar_telefone)

        # check button
        self._cb_maiusculo = False
        self._check_button_maiusculo = Checkbutton(instancia, text = "Converter para maiusculo", command=self.click_maiusculo)

        self._cb_acentuacao = False
        self._check_button_acentuacao = Checkbutton(instancia, text = "Remover acentuação", command=self.click_acentuacao )

        # empacotar
        self.tx.pack(expand=True, fill='both')
        self.tx2.pack(expand=True, fill='both')
        self._check_button_maiusculo.pack(side=LEFT)
        self._check_button_acentuacao.pack(side=LEFT)
        self.caixa_texto.pack(side=LEFT)
        self.bt1.pack(side=LEFT)
        self.bt2.pack(side=LEFT)


    def _remove_acentuacao(self, palavra):
        nfkd = unicodedata.normalize('NFKD', palavra)
        return u"".join([c for c in nfkd if not unicodedata.combining(c)])

    def tratar_nome(self):

        # limpa texto da caixa dois
        self.tx2.delete(1.0, END)

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

        # limpa texto caixa um
        self.tx.delete(1.0, END)

    def click_maiusculo(self):
        """define se sera convertido para muiusculo"""
        self._cb_maiusculo = not self._cb_maiusculo

    def click_acentuacao(self):

        self._cb_acentuacao = not self._cb_acentuacao

    def _retorna_apenas_numeros(self, texto):

        return re.sub("[^0-9]", "", texto)

    def _remove_zeros_inicial(self, texto):

        return re.sub("^0*", "", texto)

    def _verifica_ddd(self, texto):

        if (len(texto) == 8 or len(texto) == 9) and (len(self.caixa_texto.get()) == 2):
            return self.caixa_texto.get() + texto
        else:
            return texto

    def _verifica_nove(self, texto):

        if len(texto) == 11:
            # 31986618477
            return texto

        if len(texto) == 10:
            # 3186618477
            return texto[0:2] + "9" + texto[2:]

        return texto

    def _retorna_telefone_valido(self, texto):

        # 31986618477
        # 3186618477
        if len(texto) == 11 or len(texto) == 10:
            return texto
        else:
            return "0"

    def tratar_telefone(self):

        self.tx2.delete(1.0, END)

        linhas = self.tx.get(1.0, END).split("\n")

        numeros = []

        for linha in linhas[:-1]:
            print(linha)

            # tira tudo que for diferente de 0 a 9
            linha = self._retorna_apenas_numeros(linha)

            # tirar todos os 0 do inicio da
            linha = self._remove_zeros_inicial(linha)

            # insere ou nao ddd
            linha = self._verifica_ddd(linha)

            # verificar se precisa adicionar o numero 9
            linha = self._verifica_nove(linha)

            # valida telefone
            linha = self._retorna_telefone_valido(linha)

            numeros.append(linha)

        self.tx2.insert(END, "\n".join(numeros))

        # limpa texto caixa um
        self.tx.delete(1.0, END)

janela = Tk()
ManipulaTexto(instancia=janela)

janela.geometry("1000x800+200+200")
janela.mainloop()