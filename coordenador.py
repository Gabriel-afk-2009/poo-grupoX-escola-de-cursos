from pessoa import Pessoa


class Coordenador(Pessoa):
    """Coordenador responsável por uma área da escola."""

    def __init__(self, nome, idade, area, salario_base, bonus):
        """Cria um coordenador, chamando o construtor da classe Pessoa."""
        super().__init__(nome, idade)
        self.__area = area
        self.__salario_base = salario_base
        self.__bonus = bonus
