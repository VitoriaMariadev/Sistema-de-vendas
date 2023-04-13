import PySimpleGUI as sg
import bd.conect as ct
from venda.lista_vendas import*
from venda.adicionar_vendas import*
from venda.excluir_vendas import*
from venda.editar_vendas import*

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
            try:
                valor = valores['valor'][0]
            except:
                valor = '1'
            break
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
            listagem_l(f'{valor}')
            lista_vendas()
            # .un_hide abre vendas() novamente, ou a janela aberta anteriormente
            janela.un_hide()
        elif eventos == 'Adicionar vendas':
            janela.hide()
            adicionar_vendas()
            janela.un_hide()
        elif eventos == 'Editar vendas':
            listagem_v()
            janela.hide()
            listagem(f'{valor}')
            editar_vendas()
            janela.un_hide()
        elif eventos == 'Excluir vendas':
            listagem_v()
            janela.hide()
            listagem_edit(f'{valor}')
            excluir_vendas()
            janela.un_hide()
    janela.close()
