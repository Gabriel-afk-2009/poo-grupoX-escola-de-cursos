from pessoa import Pessoa

class Coordenador(Pessoa):

    def __init__(self, nome, idade, area, salario_base, bonus):

        super().__init__(nome, idade)
        self.__area = area
        self.__salario_base = salario_base
        self.__bonus = bonus

    @property
    def area(self):

        return self.__area

    def organizar_grade(self):

        return f"{self.nome} está organizando a grade de {self.__area}."

    def calcular_valor_mensal(self):

        return self.__salario_base + self.__bonus

    def __str__(self):

        return f"[Coordenador] {super().__str__()} | Área: {self.__area}"