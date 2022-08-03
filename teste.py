import PySimpleGUI as sg

layout = [
    [sg.Text("Estatísticas do Coronavírus")],
    [sg.Text('Infectados:')],
    [sg.Text('', key='infectados_output')],
    [sg.InputCombo(['Brasil', 'Estados Unidos', 'México', 'Argentina', 'Canadá'], size=(20, 3))],
    [sg.Button('Pesquisar')],
]

window = sg.Window('Estatísticas do Coronavírus', layout, size=(500, 500))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()