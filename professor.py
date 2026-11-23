from pessoa import Pessoa

class Professor(Pessoa):

    def __init__(self, nome, idade, disciplina, horas_aula, valor_hora):
        super().__init__(nome, idade)
        self.__disciplina = disciplina
        self.__horas_aula = horas_aula
        self.__valor_hora = valor_hora

    @property
    def disciplina(self):
        return self.__disciplina

    def dar_aula(self):
        return f"{self.nome} está dando aula de {self.__disciplina}."

    def calcular_valor_mensal(self):
        return self.__horas_aula * self.__valor_hora

    def __str__(self):
        return f"[Professor] {super().__str__()} | Disciplina: {self.__disciplina}"
