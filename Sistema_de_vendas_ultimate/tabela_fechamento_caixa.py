import PySimpleGUI as sg
import conect as ct
conexao = ct.Connection()
maxId = conexao.query("SELECT COUNT(*) FROM fechamento_caixa")

def listagem_C():
    """
    Função para lista os valore da tebela venda e colocar em uma variavel. Isso é necessario
    para que seja possivel colocar na tabela.
    """
    global lista_de_vendas
    lista_de_vendas = []
    pessoas = conexao.query(f'SELECT id, horaabertura, dataabertura, horafecha, datafecha, dinhinicial, dinhrecebido, dinhfinal FROM "fechamento_caixa"')
    for id, horaabertura, dataabertura, horafecha, datafecha, dinhinicial, dinhrecebido, dinhfinal  in pessoas:
        lista = []
        lista.append(id)
        lista.append(horaabertura)
        lista.append(dataabertura)
        lista.append(horafecha)
        lista.append(datafecha)
        lista.append(dinhinicial)
        lista.append(dinhrecebido)
        lista.append(dinhfinal)
        lista_de_vendas.append(lista)
      
        
def lista_caixa():
    '''
    Função para listar as vendas
    '''
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Lista de Vendas', font=('Arial 16'))],
                [sg.Table(values=lista_de_vendas,
                headings=['Caixa', 'H. Abertura', 'D. Abertura', 'H. Fechamento', 'D. Fechamento','Dinheiro Inicial','Dinheiro Recebido','Dinheiro Final'],
                max_col_width=25,
                auto_size_columns=True,
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
