from tkinter import *
from tkinter.ttk import Combobox

janela = Tk()

##PRESETS
fonte_padrao = {"font": (None, 16)}
padding10x = {"padx":10, "pady": 10}
fonte_branca = {"fg":"white"}
fundo_branco = {"fg":"black", "bg":"white"}

##PRIMEIRA LINHA - Título
texto_titulo = Label(janela, text="Estatísticas do COVID-19", font=(None, 20))
texto_titulo.grid(column=1, row=0)

##SEGUNDA LINHA - Estatísticas
texto_infectados = Label(janela, text="Infectados", **fonte_branca, bg="orange", **fonte_padrao)
texto_infectados.grid(column=0, row=1)

texto_recuperados = Label(janela, text="Recuperados", **fonte_branca, bg="green", **fonte_padrao)
texto_recuperados.grid(column=1, row=1)

texto_mortes = Label(janela, text="Mortes", **fonte_branca, bg="red", **fonte_padrao)
texto_mortes.grid(column=2, row=1)

##TERCEIRA LINHA - Output dos valores
quantidade_infectados = Label(janela, text="----", **fonte_padrao)
quantidade_infectados.grid(column=0, row=2)

quantidade_recuperados = Label(janela, text="----", **fonte_padrao)
quantidade_recuperados.grid(column=1, row=2)

quantidade_mortes = Label(janela, text="----", **fonte_padrao)
quantidade_mortes.grid(column=2, row=2)

##QUARTA LINHA - Input do país
paises = ("Brasil", "Estados Unidos", "Canadá", "Espanha", "Alemanha", "China")
seletor = Combobox(janela, values=paises)
seletor.grid(column=1, row=3)

botao = Button(janela, text="Consultar", **fonte_padrao)
botao.grid(column=2, row=3)

janela.mainloop()