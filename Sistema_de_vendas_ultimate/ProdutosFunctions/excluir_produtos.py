import PySimpleGUI as sg
import conect as ct

conexao = ct.Connection()

def listagem_prod():
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

def excluir_produtos():
    global valores
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Excluir Produtos', font=('Arial 16'))],
                [sg.Table(values=lista_de_produtos,
                headings=['Id', 'Nome', 'Preço'],
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
            nova_lista = []
            print(valores['-TABLE-'][0])
            conf = sg.popup_ok_cancel('Deseja Apagar?')
            if conf == 'OK':
                # Apagando o valor escolhido
                selected_row_index = valores['-TABLE-'][0]
                contact_information = lista_de_produtos[selected_row_index]
                id = contact_information[0]
                conexao.execute(f"DELETE FROM public.produto WHERE id = {id};")
                break


    janela.close()