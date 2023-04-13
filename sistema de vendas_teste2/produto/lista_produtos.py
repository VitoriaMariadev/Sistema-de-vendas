import PySimpleGUI as sg
import bd.conect as ct

conexao = ct.Connection()


def listagem():
    '''
    Função para colocar os produtos em uma lista para que possa ser colocado na tabela
    '''
    global lista_de_produtos 
    lista_de_produtos = []
    pessoas = conexao.query(f'select * from produto')
    for id, nome, preco in pessoas:
        lista = []
        lista.append(id)
        lista.append(nome)
        lista.append(preco)
        lista_de_produtos.append(lista)

def lista_produtos():
    '''
    Função para listar produtos
    '''
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Lista de Produtos', font=('Arial 16'))],
                [sg.Table(values=lista_de_produtos,
                headings=['id','Nome','Preço'],
                max_col_width=25,
                auto_size_columns=False,
                justification='center',
                num_rows=20,
                key='-TABLE-',
                tooltip='This is a table')],
                [sg.Button('Voltar')]
            ]

    janela = sg.Window('Produtos', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar':
            break
    janela.close()


