class Escola:
    def __init__(self, nome):
        self.__nome = nome
        self.__pessoas = []

    @property
    def nome(self):
        return self.__nome

    def cadastrar(self, pessoa):
        self.__pessoas.append(pessoa)

    def listar(self):
        if not self.__pessoas:
            print("Nenhuma pessoa cadastrada.")
            return

        for pessoa in self.__pessoas:
            print(pessoa)

    def buscar_por_nome(self, nome):
        return [
            p for p in self.__pessoas
            if nome.lower() in p.nome.lower()
        ]

    def executar_acao_polimorfica(self):
        for pessoa in self.__pessoas:
            valor = pessoa.calcular_valor_mensal()
            print(f"{pessoa.nome}: R$ {valor:.2f}")

    def __str__(self):
        return f"Escola {self.__nome} ({len(self.__pessoas)} pessoas)"