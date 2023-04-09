import PySimpleGUI as sg
import bd.conect as ct
from produto.lista_produtos import*
from produto.adicionar_produtos import*
from produto.editar_produtos import*
from produto.excluir_produtos import*
conexao = ct.Connection()

def produtos():
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Produtos', font=('Arial 16'))],
                [sg.Button('Ver produtos', size=(25,0))],
                [sg.Button('Adicionar produtos', size=(25,0))],
                [sg.Button('Editar produtos', size=(25,0))],
                [sg.Button('Excluir produtos', size=(25,0))],
                [sg.Button('Voltar', size=(25,0))]
            ]

    janela = sg.Window('Produtos', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar': 
            break
        elif eventos == 'Ver produtos':
            janela.hide()
            listagem()
            lista_produtos()
            janela.un_hide()
        elif eventos == 'Adicionar produtos':
            janela.hide()
            adicionar_produtos()
            janela.un_hide()
        elif eventos == 'Editar produtos':
            janela.hide()
            editar_produtos()
            janela.un_hide()
        elif eventos == 'Excluir produtos':
            janela.hide()
            excluir_produtos()
            janela.un_hide()
    janela.close()
