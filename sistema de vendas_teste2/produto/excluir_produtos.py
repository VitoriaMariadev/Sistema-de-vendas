import PySimpleGUI as sg
import bd.conect as ct
conexao = ct.Connection()

def apagar(tabela='produto'):
    '''
    Função para apagar os produtos.
    '''
    # Pegando o valor da jenela e colocando em uma variavel.
    id = valores['id']
    conexao.execute(f"DELETE FROM public.{tabela} WHERE id = {id};")

def excluir_produtos():
    global valores
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Excluir Produtos', font=('Arial 16'))],
                [sg.Text('Id do produto', size=(10,1)), sg.Input(key='id')],
                [sg.Button('Excluir'), sg.Push(), sg.Button('Voltar')]
            ]

    janela = sg.Window('Produtos', layout, element_justification='c', size=(400,110))

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar': 
            break
        elif eventos == 'Excluir':
            apagar()
            sg.popup('Produto Apagado')
            # Deixando a janela em branco
            janela['id'].update('')
    janela.close()