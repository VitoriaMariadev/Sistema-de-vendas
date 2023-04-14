import PySimpleGUI as sg
import conect as ct

from VendasFunctions.adicionar import *
from VendasFunctions.editar import *
from VendasFunctions.excluir import *
from VendasFunctions.lista_vendas import *
from VendasFunctions.listar_produtos import *

conexao = ct.Connection()

def listagem_v():
    '''
    Função para listar as vendas que existem no banco de dados.
    '''
    global valor
    global lista_de_vendas

    lista_de_vendas = []
    pessoas = conexao.query(f'SELECT id_venda FROM public.venda;')
    for id_venda in pessoas:
        lista_de_vendas.append(id_venda)
    
    lista = []
    for i in lista_de_vendas:
        if i not in lista:
            lista.append(i)
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Vendas', font=('Arial 16'))],
                [sg.Combo(lista, key='valor', size=(25,0))],
                [sg.Button('OK')]
            ]

    janela = sg.Window('Vendas', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED: 
            break
        if eventos == 'OK':
            if 'valor' == '':
                sg.popup('Nenhuma venda selecionada')
            try:
                valor = valores['valor'][0]
                break
            except:
                sg.popup('Nenhuma venda selecionada')
            
    janela.close()

def vendas():
    '''
    Função venda responsavel por chamar todas as outras funções.
    '''
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Vendas', font=('Arial 16'))],
                [sg.Button('Ver vendas', size=(25,0))],
                [sg.Button('Adicionar vendas', size=(25,0))],
                [sg.Button('Editar vendas', size=(25,0))],
                [sg.Button('Excluir vendas', size=(25,0))],
                [sg.Button('Voltar', size=(25,0))]
            ]

    janela = sg.Window('Vendas', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar': 
            break
        elif eventos == 'Ver vendas':
            listagem_v()
            # .hide fecha o vendas() ou a janela atual
            janela.hide()
            try:
                listagem_l(f'{valor}')
                lista_vendas()
            except:
                pass
            # .un_hide abre vendas() novamente, ou a janela aberta anteriormente
            janela.un_hide()
        elif eventos == 'Adicionar vendas':
            janela.hide()
            adicionar_vendas()
            janela.un_hide()
        elif eventos == 'Editar vendas':
            listagem_v()
            janela.hide()
            try:
                listagem(f'{valor}')
                editar_vendas()
            except:
                pass
            janela.un_hide()
        elif eventos == 'Excluir vendas':
            listagem_v()
            janela.hide()
            try:
                listagem_edit(f'{valor}')
                excluir_vendas()
            except:
                pass
            janela.un_hide()
    janela.close()