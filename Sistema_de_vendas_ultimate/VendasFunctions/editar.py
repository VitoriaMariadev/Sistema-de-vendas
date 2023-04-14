import PySimpleGUI as sg
import conect as ct
from VendasFunctions.listar_produtos import *

conexao = ct.Connection()

def interface_listagem():
    '''
    Função para criar uma tabela de lista de vendas
    '''
    global valor_nome
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Produto', font=('Arial 16'))],
                [sg.Combo(lista_de_produtos, key='valor', size=(25,0))],
                [sg.Button('OK')]
            ]

    janela = sg.Window('Vendas', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED: 
            break
        if eventos == 'OK':
            valor_nome = valores['valor']
            break
    janela.close()

def listagem(tabela):
    '''
    Função para pegar os valores que tem em uma tabela e colocar em uma lista, são os valores da tabela.
    '''
    global id_venda
    id_venda = tabela
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

def editar_vendas():
    '''
    Fução para editar vendas
    '''
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Editar Vendas', font=('Arial 16'))],
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
            selected_row_index = valores['-TABLE-'][0]
            contact_information = lista_de_vendas[selected_row_index]
            interface_listagem()
            nova_quantidade = sg.popup_get_text('Nova quantidade: ', size=(15,10))
            nova_quantidade = int(nova_quantidade)
            id_v = sg.popup_get_text('Novo Id: ')
            id_p = lista_nome.index(valor_nome[0])
            id_produto = lista_id[id_p]
            str(id_produto)
            valor_p = ''
            pessoas = conexao.query('SELECT id, nome, preco FROM "produto" p')
            # Quebrando o 'money' para transformar em float.
            for id, nome, preco in pessoas:
                if id == id_produto:
                    for v in preco[2:-1]:
                        if v == ',':
                            valor_p+= '.'
                        else:
                            valor_p += v
            print(valor_p)
            valor_total = nova_quantidade*float(valor_p)
            conexao.execute(f"UPDATE public.venda SET id_v={id_v}, id_venda={id_venda}, id_produto={id_produto}, quantidade={nova_quantidade}, valor={valor_total} WHERE id_v = {contact_information[0]};")
    janela.close()
