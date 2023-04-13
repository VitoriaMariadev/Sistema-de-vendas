import PySimpleGUI as sg
import bd.conect as ct
from produto.produtos import*
from venda.vendas import*
import time
conexao = ct.Connection()
caixa = False
tempo_aberto = []
sg.theme('Default')
sg.set_options(font=('Arial 12'), text_color='black')

layout = [  
            [sg.Text('Sistema de Vendas', font=('Arial 16'))],
            [sg.Button('Produtos', size=(25,0))],
            [sg.Button('Vendas', size=(25,0), button_color='grey')],
            [sg.Button('Fechamento de caixa', size=(25,0))],
            [sg.Button('Encerrar', size=(25,0))]
        ]

janela = sg.Window('Menu', layout, element_justification='c', size = (300,200))

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Encerrar': 
        break
    elif eventos == 'Produtos':
        janela.hide()
        produtos()
        janela.un_hide()
    elif eventos == 'Fechamento de caixa':
        janela.hide()
        #======================================================================================================================
        # Fechamento de caixa que eu não consegui exporta de outra pasta
        sg.theme('Default')
        sg.set_options(font=('Arial 12'), text_color='black')

        layout = [  
                    [sg.Text('Fechamento de Caixa', font=('Arial 16'))],
                    [sg.Button('Abrir Caixa', size=(25,0))],
                    [sg.Button('Voltar', size=(25,0))]
                ]

        janela_c = sg.Window('Fechamento de caixa', layout, element_justification='c')

        while True:
            eventos, valores = janela_c.read()
            if eventos == sg.WIN_CLOSED or eventos == 'Voltar': 
                break

            if caixa == False:
                if eventos == 'Abrir Caixa':
                    if caixa == False:
                        caixa = True
                        sg.popup('Caixa Aberto')
                        t = time.localtime(time.time())
                        localtime = time.asctime(t)
                        tempo_aberto.append(localtime)
                        # Modificando a cor do botão
                        janela['Vendas'].update(button_color='#0c2464')

            elif caixa == True:
                if eventos == 'Abrir Caixa':
                    sg.popup('Caixa Fechado')
                    caixa = False
                    janela['Vendas'].update(button_color='grey')
        janela_c.close()
        #========================================================================================================================
        janela.un_hide()
    elif eventos == 'Vendas':
        if caixa == True:
            janela.hide()
            vendas()
            janela.un_hide()
        else:
            sg.popup('Caixa fechado')


janela.close()
