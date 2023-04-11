import PySimpleGUI as sg
import bd.conect as ct

conexao = ct.Connection()

def listagem_l(tabela):
    global lista_de_vendas
    lista_de_vendas = []
    pessoas = conexao.query(f'SELECT nome, quantidade, valor FROM "venda" a, "produto" p WHERE a.id_produto = p.id and a.id_venda = {tabela}')
    for nome, quantidade, valor in pessoas:
        lista = []
        lista.append(nome)
        lista.append(quantidade)
        lista.append(valor)
        lista_de_vendas.append(lista)

def lista_vendas():
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Lista de Vendas', font=('Arial 16'))],
                [sg.Table(values=lista_de_vendas,
                headings=['Nome','Quantidade','Valor Total'],
                max_col_width=25,
                auto_size_columns=False,
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
    janela.close()

