from tkinter import *

##  [sg.Text('Estatísticas do COVID-19')],
##  [sg.Text('Infectados'),sg.Text('Recuperados'),sg.Text('Mortes')],
##  [sg.Text('*'),sg.Text('*'),sg.Text('*')],
##  [sg.Text('*'),sg.Text('*'),sg.Text('*')]

janela = Tk()

##PRIMEIRA LINHA - Título
texto_titulo = Label(janela, text="Estatísticas do COVID-19")
texto_titulo.grid(column=1, row=0)

##SEGUNDA LINHA - Estatísticas
texto_infectados = Label(janela, text="Infectados")
texto_infectados.grid(column=0, row=1)

texto_recuperados = Label(janela, text="Recuperados")
texto_recuperados.grid(column=1, row=1)

texto_mortes = Label(janela, text="Mortes")
texto_mortes.grid(column=2, row=1)

##TERCEIRA LINHA - Output dos valores
quantidade_infectados = Label(janela, text="----")
quantidade_infectados.grid(column=0, row=2)

quantidade_recuperados = Label(janela, text="----")
quantidade_recuperados.grid(column=1, row=2)

quantidade_mortes = Label(janela, text="----")
quantidade_mortes.grid(column=2, row=2)

##QUARTA LINHA - Input do país
botao = Button(janela, text="Consultar")
botao.grid(column=2, row=3)

janela.mainloop()