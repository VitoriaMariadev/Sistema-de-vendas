import PySimpleGUI as sg
import bd.conect as ct
conexao = ct.Connection()

def cadastrar(tabela):
    id = valores['id']
    nome = valores['nome']
    preco = valores['preco']
    conexao.execute(f"INSERT INTO public.{tabela}(id, nome, preco) VALUES ({id}, '{nome}', {preco});")

def adicionar_produtos():
    global valores
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Adicionar Produtos', font=('Arial 16'))],
                [sg.Text('Id', size=(5,1)), sg.Input(key='id')],
                [sg.Text('Nome', size=(5,1)), sg.Input(key='nome')],
                [sg.Text('Preço', size=(5,1)), sg.Input(key='preco')],
                [sg.Button('Adicionar'), sg.Push(), sg.Button('Voltar')]
            ]

    janela = sg.Window('Produtos', layout, element_justification='c', size=(400,170))

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar': 
            break
        elif eventos == 'Adicionar':
            cadastrar('produto')
            sg.popup('Produto Cadastrado')
            janela['id'].update('')
            janela['nome'].update('')
            janela['preco'].update('')
    janela.close()
