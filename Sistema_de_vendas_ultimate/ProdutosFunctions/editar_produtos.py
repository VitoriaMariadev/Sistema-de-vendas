import PySimpleGUI as sg
import conect as ct

conexao = ct.Connection()

def alterar(tabela= 'produto'):
    '''
    Função para alterar os produtos adicionados na tabela.
    '''
    id = conexao.query(f"SELECT id FROM produto WHERE nome = '{valores['produto'][0]}'")
    #id = valores['produto']
    nome = valores['nome']
    preco = valores['preco']
    conexao.execute(f"UPDATE public.{tabela} SET id={id[0][0]}, nome='{nome}', preco={preco} WHERE id = {id[0][0]};")

def editar_produtos():
    '''
    Função para editar os produtos
    '''
    global valores

    lista_de_produtos = []
    produtos = conexao.query("SELECT nome FROM produto")
    for nome in produtos:
        lista_de_produtos.append(nome)

    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Editar Produtos', font=('Arial 16'))],
                [sg.Text('Id do produto', size=(10,1)), sg.Combo(lista_de_produtos, key='produto', size=(25,0))],
                [sg.Text('Novo nome', size=(10,1)), sg.Input(key='nome')],
                [sg.Text('Novo preço', size=(10,1)), sg.Input(key='preco')],
                [sg.Button('Alterar'), sg.Push(), sg.Button('Voltar')]
            ]

    janela = sg.Window('Produtos', layout, element_justification='c', size=(400,170))

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar': 
            break
        elif eventos == 'Alterar':
            # Chamando a função para alterar os produtos de acordo com o que foi preenchido.
            alterar()
            sg.popup('Produto Alterado')
            # Deixando as janelas em branco
            janela['produto'].update('')
            janela['nome'].update('')
            janela['preco'].update('')
    janela.close()