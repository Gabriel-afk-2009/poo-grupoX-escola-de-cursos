class Pessoa:
    "CLASSE QUE REPRESENTA A PESSOA DA ESCOLA"

    def __init__(self, nome, idade):
        "CRIA UMA PESSOA COM NOME E IDADE"
        self.nome = nome    # usa o setter, então já valida
        self.idade = idade

    @property
    def nome(self):
        "VOLTA O NOME DA PESSOA"
        return self.__nome

    @nome.setter
    def nome(self, valor):
        "NAO PERMITE A PESSOA NAO TER NOME"
        if not valor.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = valor.strip()

    @property
    def idade(self):

        return self.__idade

    @idade.setter
    def idade(self, valor):

        if valor < 0:
            raise ValueError("A idade não pode ser negativa.")
        self.__idade = valor

    def calcular_valor_mensal(self):

        return 0.0

    def __str__(self):

        return f"{self.__nome}, {self.__idade} anos"