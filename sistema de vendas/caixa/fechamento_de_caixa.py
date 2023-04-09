import PySimpleGUI as sg
import bd.conect as ct
conexao = ct.Connection()

def fechamento_de_caixa():
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Fechamento de Caixa', font=('Arial 16'))],
                [sg.Button('Ver dias', size=(25,0))],
                [sg.Button('Voltar', size=(25,0))]
            ]

    janela = sg.Window('Fechamento de caixa', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar': 
            break
        elif eventos == 'Ver dias':
            pass
    janela.close()
