import PySimpleGUI as sg
import conect as ct
from VendasFunctions.listar_produtos import *

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
    id = conexao.query("SELECT COUNT(id_v) FROM venda")
    caixa_atual = conexao.query("SELECT max(id) FROM fechamento_caixa")
    id_venda = valores['id_venda']
    quantidade = int(valores['quantidade'])
    valor_total = quantidade*float(valor)
    
    
    #dinhrecebido = conexao.query(f"SELECT dinhrecebido FROM fechamento_caixa WHERE id = {caixa_atual}")
    
    #conexao.execute(f"UPDATE fechamento_caixa SET dinhrecebido = SUM()")
    
    conexao.execute(f"INSERT INTO public.venda(id_v, id_caixa, id_venda, id_produto, quantidade, valor) VALUES ({id[0][0]+1}, {caixa_atual[0][0]}, {id_venda}, {id_novo}, {quantidade}, {valor_total});")
    
def adicionar_vendas():

    '''
    Função para adicionar vendas
    '''
    
    global valores
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Adicionar Vendas', font=('Arial 16'))],
                [sg.Text('Id da venda', size=(10,1)), sg.Input(key='id_venda')],
                [sg.Text('Produto', size=(10,1)), sg.Combo(lista_de_produtos, key='id_produto', size=(25, 0)), sg.Push()],
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
            try:
                cadastrar('venda')
                sg.popup('Venda Cadastrado')
                janela['id_venda'].update('')
                janela['id_produto'].update('')
                janela['quantidade'].update('')
            except:
                sg.popup('Elementos faltando')
            
            caixa_atual = conexao.query("SELECT max(id) FROM fechamento_caixa")
            valor_vendas = conexao.query("SELECT SUM(valor) FROM venda")
            if valor_vendas == [(None,)] or valor_vendas == 'None' or valor_vendas == None:
                valor_vendas = '0'
            
            somas = conexao.query(f"SELECT SUM(valor) FROM venda WHERE id_caixa = {caixa_atual[0][0]}")
            
            print(somas)
            
            valor_vendas = str(valor_vendas[0][0])

            conexao.execute(f"UPDATE fechamento_caixa SET dinhrecebido = '{somas[0][0]}' WHERE id = {caixa_atual[0][0]}")

    janela.close()

