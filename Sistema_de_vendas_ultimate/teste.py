import conect as ct

conexao = ct.Connection()

def cadastrar():

    '''
    Função para transformar o 'money' em float
    '''

    global valor
    valor = ''
    id_produto = 1
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
    id_venda = 2
    quantidade = 2
    valor_total = quantidade*2
    
    
    #dinhrecebido = conexao.query(f"SELECT dinhrecebido FROM fechamento_caixa WHERE id = {caixa_atual}")
    
    #conexao.execute(f"UPDATE fechamento_caixa SET dinhrecebido = SUM()")
    
    conexao.execute(f"INSERT INTO public.venda(id_v, id_caixa, id_venda, id_produto, quantidade, valor) VALUES ({id[0][0]+1}, {caixa_atual[0][0]}, {id_venda}, {id_novo}, {quantidade}, {valor_total});")
    
    valor_vendas = conexao.query("SELECT SUM(valor) FROM venda")
    
    conexao.execute(f"UPDATE fechamento_caixa SET dinhrecebido = dinhrecebido + 'R$ {valor_vendas}' WHERE id = {caixa_atual[0][0]}")
    
    print(valor_vendas)
    
cadastrar()