from tkinter import *

janela = Tk()

##PRESETS
fonte_padrao = {"font": (None, 16)}
padding10x = {"padx":10, "pady": 10}
fonte_branca = {"fg":"white"}
fundo_branco = {"fg":"black", "bg":"white"}

##PRIMEIRA LINHA - Título
texto_titulo = Label(janela, text="Estatísticas do COVID-19", font=(None, 20))
texto_titulo.grid(column=1, row=0, **padding10x)

##SEGUNDA LINHA - Estatísticas
texto_infectados = Label(janela, text="Infectados", **fonte_branca, bg="yellow", **fonte_padrao)
texto_infectados.grid(column=0, row=1, **padding10x)

texto_recuperados = Label(janela, text="Recuperados", **fonte_branca, bg="green", **fonte_padrao)
texto_recuperados.grid(column=1, row=1, **padding10x)

texto_mortes = Label(janela, text="Mortes", **fonte_branca, bg="red", **fonte_padrao)
texto_mortes.grid(column=2, row=1, **padding10x)

##TERCEIRA LINHA - Output dos valores
quantidade_infectados = Label(janela, text="----", **fonte_padrao)
quantidade_infectados.grid(column=0, row=2, **padding10x)

quantidade_recuperados = Label(janela, text="----", **fonte_padrao)
quantidade_recuperados.grid(column=1, row=2, **padding10x)

quantidade_mortes = Label(janela, text="----", **fonte_padrao)
quantidade_mortes.grid(column=2, row=2, **padding10x)

##QUARTA LINHA - Input do país
botao = Button(janela, text="Consultar", **fonte_padrao)
botao.grid(column=2, row=3, **padding10x)

janela.mainloop()