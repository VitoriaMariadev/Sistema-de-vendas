import PySimpleGUI as sg
import conect as ct
from VendasFunctions.lista_vendas import *

conexao = ct.Connection()

def listagem_edit(tabela):
    '''
    função para pegar os valores da tabela e colocar em uma lista
    '''
    global lista_de_vendas
    lista_de_vendas = []
    pessoas = conexao.query(f'SELECT id_v, nome, quantidade, valor FROM "venda" a, "produto" p WHERE a.id_produto = p.id and a.id_venda = {tabela}')
    for id_v, nome, quantidade, valor in pessoas:
        lista = []
        lista.append(id_v)
        lista.append(nome)
        lista.append(quantidade)
        lista.append(valor)
        lista_de_vendas.append(lista)

def excluir_vendas():
    '''
    Função para excluir vendas
    '''
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Excluir Vendas', font=('Arial 16'))],
                [sg.Table(values=lista_de_vendas,
                headings=['Id','Nome','Quantidade','Valor Total'],
                max_col_width=25,
                auto_size_columns=False,
                enable_events=True,
                justification='center',
                num_rows=20,
                key='-TABLE-',
                tooltip='This is a table')],
                [sg.Button('Voltar')]
            ]

    janela = sg.Window('Vendas', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar':
            break
        elif eventos == '-TABLE-':
            nova_lista = []
            print(valores['-TABLE-'][0])
            conf = sg.popup_ok_cancel('Deseja Apagar?')
            if conf == 'OK':
                # Apagando o valor escolhido
                selected_row_index = valores['-TABLE-'][0]
                contact_information = lista_de_vendas[selected_row_index]
                id = contact_information[0]
                conexao.execute(f"DELETE FROM public.venda WHERE id_v = {id};")
                break
            else:
                pass


    janela.close()

