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

