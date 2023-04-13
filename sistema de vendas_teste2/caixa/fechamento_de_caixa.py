import time
import PySimpleGUI as sg
# mport bd.conect as ct
# conexao = ct.Connection()


def fechamento_de_caixa():
    '''
    Tentativa de chamar a função caixa em outro arquivo. Tentativa falha.
    '''
    global caixa
    caixa = False
    tempo_aberto = []
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Fechamento de Caixa', font=('Arial 16'))],
                [sg.Button('Abrir Caixa', size=(25,0))],
                [sg.Button('Voltar', size=(25,0))]
            ]

    janela = sg.Window('Fechamento de caixa', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar': 
            break

        if caixa == False:
            if eventos == 'Abrir Caixa':
                if caixa == False:
                    caixa == True
                    sg.popup('Caixa Aberto')
                    t = time.localtime(time.time())
                    localtime = time.asctime(t)
                    tempo_aberto.append(localtime)

        elif caixa == True:
            if eventos == 'Abrir Caixa':
                sg.popup('Caixa Fechado')
                caixa == False

    janela.close()





