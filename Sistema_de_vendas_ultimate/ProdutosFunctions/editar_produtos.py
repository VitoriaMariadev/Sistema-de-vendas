import PySimpleGUI as sg
import conect as ct

conexao = ct.Connection()

def listagem_prod_edit():
    '''
    função para pegar os valores da tabela e colocar em uma lista
    '''
    global lista_de_produtos
    lista_de_produtos = []
    pessoas = conexao.query(f'SELECT id, nome, preco FROM produto')
    for id, nome, preco in pessoas:
        lista = []
        lista.append(id)
        lista.append(nome)
        lista.append(preco)
        lista_de_produtos.append(lista)

def editar_produtos():
    '''
    Função para editar os produtos
    '''
    global valores

    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Editar Produtos', font=('Arial 16'))],
                [sg.Table(values=lista_de_produtos,
                headings=['id', 'nome', 'preco'],
                max_col_width=25,
                auto_size_columns=False,
                enable_events=True,
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
        elif eventos == '-TABLE-':
            selected_row_index = valores['-TABLE-'][0]
            contact_information = lista_de_produtos[selected_row_index]
            novo_nome = sg.popup_get_text('Nova nome: ', size=(15,10))
            id = conexao.query("SELECT COUNT(*) FROM fechamento_caixa")
            novo_preco = sg.popup_get_text('Novo Preço: ', size=(15,10))
            conexao.execute(f"UPDATE public.produto SET id={id[0][0]+1}, nome='{novo_nome}', preco='{novo_preco}' WHERE id = {contact_information[0]};")

    janela.close()