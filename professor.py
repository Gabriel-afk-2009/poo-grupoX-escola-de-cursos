from pessoa import Pessoa


class Professor(Pessoa):
    """Professor que dá aulas em uma disciplina."""

    def __init__(self, nome, idade, disciplina, horas_aula, valor_hora):
        """Cria um professor, chamando o construtor da classe Pessoa."""
        super().__init__(nome, idade)
        self.__disciplina = disciplina
        self.__horas_aula = horas_aula
        self.__valor_hora = valor_hora