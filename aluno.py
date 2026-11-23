from pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, idade, curso, mensalidade):

        super().__init__(nome, idade)
        self.__curso = curso
        self.mensalidade = mensalidade

    @property
    def curso(self):
        return self.__curso

    @property
    def mensalidade(self):
        return self.__mensalidade

    @mensalidade.setter
    def mensalidade(self, valor):
        if valor <= 0:
            raise ValueError
        self.__mensalidade = valor

    def matricular(self, novo_curso):
        self.__curso = novo_curso
        return f"{self.nome} matriculado em {novo_curso}."

    def calcular_valor_mensal(self):

        return self.__mensalidade

    def __str__(self):
        return f"[Aluno] {super().__str__()} | Curso: {self.__curso}"