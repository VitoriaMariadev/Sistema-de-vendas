import PySimpleGUI as sg
import conect as ct
conexao = ct.Connection()
maxId = conexao.query("SELECT COUNT(*) FROM fechamento_caixa")

def listagem_C():
    """
    Função para lista os valore da tebela venda e colocar em uma variavel. Isso é necessario
    para que seja possivel colocar na tabela.
    """
    global lista_de_caixas
    lista_de_caixas = []
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
        lista_de_caixas.append(lista)
      
        
def lista_caixa():
    '''
    Função para listar as vendas
    '''
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Lista de Vendas', font=('Arial 16'))],
                [sg.Table(values=lista_de_caixas,
                headings=['Caixa', 'H. Abertura', 'D. Abertura', 'H. Fechamento', 'D. Fechamento','Dinheiro Inicial','Dinheiro Recebido','Dinheiro Final'],
                max_col_width=25,
                auto_size_columns=True,
                justification='center',
                enable_events=True,
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
            contact_information = lista_de_caixas[selected_row_index]
            opcao = sg.popup_ok_cancel('Deseja baixa a nota do caixa? ')
            if opcao == 'OK':
                with open(f'Fechamento_caixa_{maxId[0][0]}.txt', 'w') as arquivo:
                    qtd = 0
                    for valores in contact_information:
                        if qtd == 0:
                            arquivo.write(f'---Caixa---: {str(valores)}\n')
                        elif qtd == 1:
                            arquivo.write(f'Hora de Abertura: {str(valores)} |  ')
                        elif qtd == 2:
                            arquivo.write(f'Data de Abertura: {str(valores)}\n')
                        elif qtd == 3:
                            arquivo.write(f'Hora de Fechamento: {str(valores)}|  ')
                        elif qtd == 4:
                            arquivo.write(f'Data de Fechamento: {str(valores)}\n')
                        elif qtd == 5:
                            arquivo.write(f'Dinheiro Inicial: {str(valores)}\n')
                        elif qtd == 6:
                            arquivo.write(f'Dinheiro Recebido: {str(valores)}\n')
                        elif qtd == 7:
                            arquivo.write(f'>>> Dinheiro Final: {str(valores)}\n')
                        
                        qtd += 1


    janela.close()

