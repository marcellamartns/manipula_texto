# -*- coding: utf-8 -*-

from tkinter import *


def manipula():
    linhas = tx.get(1.0, END).split("\n")

    nomes = []

    for nome in linhas[:-1]:

        nome_partes = nome.split()
        primeiro_nome = nome_partes[0]
        nomes.append(primeiro_nome)
        # lb["text"] = dicionario_nomes["nome"]
        tx.mark_set(nomes, INSERT)
        tx.mark_gravity(nomes, LEFT)

    print(nomes)



    # lbn["text"] = tx.get(1.0, END)

janela = Tk()

tx = Text(janela)
tx.place(x=300, y=130)


# scrollbar = Scrollbar(tx)
# scrollbar.place(x=222, y=212)

# ed = Entry(janela)
# ed.place(x=100, y=100)

bt = Button(janela, width=20, text="ok", command=manipula)
bt.place(x=100, y=150)

lbn = Label(janela)
lbn.place(x=189, y=199)

lb = Label(janela)
lb.place(x=100, y=200)



janela.geometry("1000x800+200+200")
janela.mainloop()