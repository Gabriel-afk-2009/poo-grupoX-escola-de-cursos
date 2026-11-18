class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome    # usa o setter, então já valida
        self.idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
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