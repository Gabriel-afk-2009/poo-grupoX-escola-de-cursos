from pessoa import Pessoa


class Coordenador(Pessoa):
    """Coordenador responsável por uma área da escola."""

    def __init__(self, nome, idade, area, salario_base, bonus):
        """Cria um coordenador, chamando o construtor da classe Pessoa."""
        super().__init__(nome, idade)
        self.__area = area
        self.__salario_base = salario_base
        self.__bonus = bonus

        @property
        def area(self):
            """Retorna a área do coordenador."""
            return self.__area

        def organizar_grade(self):
            """Mostra que o coordenador está organizando a grade (método próprio)."""
            return f"{self.nome} está organizando a grade de {self.__area}."

        def calcular_valor_mensal(self):
            """Sobrescreve o método da base: salário base mais bônus."""
            return self.__salario_base + self.__bonus

        def __str__(self):
            """Retorna os dados do coordenador."""
            return f"[Coordenador] {super().__str__()} | Área: {self.__area}"

