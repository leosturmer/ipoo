class Filme:
    def __init__(self, categoria, genero):
        self.alugado = False
        self.em_acervo = True
        self.valor = 0.0
        self.classificacao = 0.0
        self.categoria = categoria
        self.genero = genero

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.multa_por_dano = 0.0
    
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.filmes_escolhidos = []
    
class Aluguel:
    def __init__(self, cliente):
        self.cliente = cliente 
        self.filmes = []
        self.data_retirada = ""
        self.data_devolucao = ""
        self.valor_aluguel = 0.0
        self.juros_atraso = 0.0

class Locadora():
    pass

class Funcionario():
    pass

def alugar_filme():
    '''
    o cliente
        - identifica-se para a locadora
    
    a locadora
        - valida o cliente

    o cliente
        - escolhe os filmes na prateleira
        - dirige-se ao funcionário com os filmes
        - identifica-se ao funcionário
     
    o funcionário
       - valida o cliente
       - registra os aluguéis dos filmes no sistema/locadora

    a locadora
        - recebe os registros de aluguel fornecidos pelo funcionário
        - calcula os prazos de devolução
        - calcula o valor total dos aluguéis
        - retorna ao funcionário os registros de aluguel preenchidos

    o funcionário
        - receb os registros preenchidos
       - dá ao cliente um comprovante do aluguel com o valor total e a data de devolução lido nos registros
    '''

    um_cliente = Cliente()
    a_locadora = Locadora()
    um_funcionario = Funcionario()

    a_locadora.validar(um_cliente)
    filmes_disponiveis = a_locadora.mostrar_filmes_da_prateleira()
    um_cliente.escolher(filmes_disponiveis)
    um_funcionario.receber_filmes(um_cliente.filmes_escolhidos)
    a_locadora.preencher_registros_de_aluguel(um_funcionario.filmes_para_alugar)





###############

lancamento = Categoria()
lancamento.nome = "Lançamento"

um_filme = Filme(lancamento)

algum_cliente = Cliente()
outro_cliente = Cliente()

um_aluguel = Aluguel(algum_cliente)

