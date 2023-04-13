import PySimpleGUI as sg
import bd.conect as ct
from teste.testes import*
conexao = ct.Connection()

def cadastrar(tabela):
    '''
    Função para transformar o 'money' em float
    '''
    global valor
    valor = ''
    id_produto = valores['id_produto'][0]
    pessoas = conexao.query('SELECT id, nome, preco FROM "produto" p')
    for id, nome, preco in pessoas:
        if nome == id_produto:
            id_novo = id
            valor = ''
            for v in preco[2:-1]:
                if v == ',':
                    valor+= '.'
                else:
                    valor += v
    # Pego os valores das janelas e coloco em variaveis
    id = valores['id']
    id_venda = valores['id_venda']
    quantidade = int(valores['quantidade'])
    valor_total = quantidade*float(valor)
    conexao.execute(f"INSERT INTO public.venda(id_v, id_venda, id_produto, quantidade, valor) VALUES ({id}, {id_venda}, {id_novo}, {quantidade}, {valor_total});")

def adicionar_vendas():
    '''
    Função para adicionar vendas
    '''
    global valores
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Adicionar Vendas', font=('Arial 16'))],
                [sg.Text('Id', size=(10,1)), sg.Input(key='id')],
                [sg.Text('Id da venda', size=(10,1)), sg.Input(key='id_venda')],
                [sg.Text('Produto', size=(10,1)), sg.Combo(lista_de_produtos, key='id_produto'), sg.Push()],
                [sg.Text('Quantidade', size=(10,1)), sg.Input(key='quantidade')],
                [sg.Button('Adicionar'), sg.Push(), sg.Button('Voltar')]
            ]

    janela = sg.Window('Vendas', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar': 
            break
        elif eventos == 'Adicionar':
            # Chamando a função cadastrar() para efetuar o cadastro no banco de dados
            cadastrar('venda')
            print(valores['id_produto'])
            sg.popup('Venda Cadastrado')
            janela['id'].update('')
            janela['id_venda'].update('')
            janela['id_produto'].update('')
            janela['quantidade'].update('')

    janela.close()



