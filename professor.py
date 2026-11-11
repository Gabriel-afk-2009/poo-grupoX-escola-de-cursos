from pessoa import Pessoa


class Professor(Pessoa):
    """Professor que dá aulas em uma disciplina."""

    def __init__(self, nome, idade, disciplina, horas_aula, valor_hora):
        """Cria um professor, chamando o construtor da classe Pessoa."""
        super().__init__(nome, idade)
        self.__disciplina = disciplina
        self.__horas_aula = horas_aula
        self.__valor_hora = valor_hora


 @property
    def disciplina(self):
        """Retorna a disciplina do professor."""
        return self.__disciplina

    def dar_aula(self):
        """Mostra que o professor está dando aula (método próprio)."""
        return f"{self.nome} está dando aula de {self.__disciplina}."

    def calcular_valor_mensal(self):
        """Sobrescreve o método da base: salário por horas dadas."""
        return self.__horas_aula * self.__valor_hora

    def __str__(self):
        """Retorna os dados do professor."""
        return f"[Professor] {super().__str__()} | Disciplina: {self.__disciplina}"