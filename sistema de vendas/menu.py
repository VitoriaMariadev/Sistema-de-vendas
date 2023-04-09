import PySimpleGUI as sg
import bd.conect as ct
from produto.produtos import*
from venda.vendas import*
from caixa.fechamento_de_caixa import*
conexao = ct.Connection()

sg.theme('Default')
sg.set_options(font=('Arial 12'), text_color='black')

layout = [  
            [sg.Text('Sistema de Vendas', font=('Arial 16'))],
            [sg.Button('Produtos', size=(25,0))],
            [sg.Button('Vendas', size=(25,0))],
            [sg.Button('Fechamento de caixa', size=(25,0))],
            [sg.Button('Encerrar', size=(25,0))]
        ]

janela = sg.Window('Menu', layout, element_justification='c')

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Encerrar': 
        break
    elif eventos == 'Produtos':
        janela.hide()
        produtos()
        janela.un_hide()
    elif eventos == 'Vendas':
        janela.hide()
        vendas()
        janela.un_hide()
    elif eventos == 'Fechamento de caixa':
        janela.hide()
        fechamento_de_caixa()
        janela.un_hide()
janela.close()