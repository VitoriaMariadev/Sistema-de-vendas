import PySimpleGUI as sg
import conect as ct

from ProdutosFunctions.adicionar_produtos import *
from ProdutosFunctions.editar_produtos import *
from ProdutosFunctions.excluir_produtos import *
from ProdutosFunctions.lista_produtos import *

conexao = ct.Connection()

def produtos():
    '''
    Função produtos que chama todas as outras funções
    '''
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
            # .hide fecha a janela atual
            janela.hide()
            try:
                listagem()
                lista_produtos()
            except:
                pass
            # .un_hide abre a janela anterior
            janela.un_hide()
        elif eventos == 'Adicionar produtos':
            janela.hide()
            adicionar_produtos()
            janela.un_hide()
        elif eventos == 'Editar produtos':
            listagem_prod_edit()
            janela.hide()
            editar_produtos()
            janela.un_hide()
        elif eventos == 'Excluir produtos':
            listagem_prod()
            janela.hide()
            excluir_produtos()
            janela.un_hide()
    janela.close()
