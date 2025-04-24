class Vendedor:
    def __init__(self, nome, email_vendedor, senha_vendedor):
        self.nome_vendedor = nome 
        self.nome_loja = ""
        self.email_vendedor = email_vendedor
        self.senha_vendedor = senha_vendedor


class Produto:
   def __init__(self, nome, preco_venda, quantidade, producao):
       self.nome_produto = nome
       self.preco_venda = preco_venda
       self.quantidade = quantidade
       self.producao = producao
       self.preco_custo = 0.0
       self.descricao_produto = ""



class Cliente:
    def __init__(self, nome_cliente, telefone_cliente, email_cliente):
        self.nome_cliente = nome_cliente
        self.telefone_cliente = telefone_cliente
        self.email_cliente = email_cliente
        self.endereco_cliente = ""
       


class Venda:
    def __init__(self, cliente_venda, data_venda, produtos_venda, entrega_venda, pagamento_venda, prazo_entrega):
        self.cliente_venda = cliente_venda
        self.data_venda = data_venda
        self.produtos_venda = produtos_venda
        self.entrega_venda = entrega_venda
        self.pagamento_venda = pagamento_venda
        self.prazo_entrega = prazo_entrega
        self.prazo_producao = 0.0
        self.comentarios_venda = ""
        self.endereco_venda = ""