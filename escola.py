class Escola:
    """Gerencia a lista de pessoas da escola."""

    def __init__(self, nome):
        """Cria a escola com uma lista vazia de pessoas."""
        self.__nome = nome
        self.__pessoas = []

    @property
    def nome(self):
        """Retorna o nome da escola."""
        return self.__nome

    def cadastrar(self, pessoa):
        """Adiciona uma pessoa à lista."""
        self.__pessoas.append(pessoa)

    def listar(self):
        """Mostra todas as pessoas cadastradas."""
        if not self.__pessoas:
            print("Nenhuma pessoa cadastrada.")
        for pessoa in self.__pessoas:
            print(pessoa)

    def buscar_por_nome(self, nome):
        """Retorna as pessoas cujo nome contém o texto buscado."""
        return [p for p in self.__pessoas if nome.lower() in p.nome.lower()]

    def executar_acao_polimorfica(self):
        """Chama o mesmo método em todos os objetos (polimorfismo)."""
        for pessoa in self.__pessoas:
            valor = pessoa.calcular_valor_mensal()
            print(f"{pessoa.nome}: R$ {valor:.2f}")

    def __str__(self):
        """Retorna o nome da escola e a quantidade de pessoas."""
        return f"Escola {self.__nome} ({len(self.__pessoas)} pessoas)"