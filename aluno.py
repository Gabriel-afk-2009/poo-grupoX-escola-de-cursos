from pessoa import Pessoa


class Aluno(Pessoa):
    "CLASSE ALUNO "

    def __init__(self, nome, idade, curso, mensalidade):
        """CRIA UM ALUNO"""
        super().__init__(nome, idade)
        self.__curso = curso
        self.mensalidade = mensalidade

    @property
    def curso(self):
        """Retorna o curso do aluno."""
        return self.__curso

    @property
    def mensalidade(self):
        """Retorna a mensalidade."""
        return self.__mensalidade

    @mensalidade.setter
    def mensalidade(self, valor):
        """Define a mensalidade. Não aceita valor menor ou igual a zero."""
        if valor <= 0:
            raise ValueError("A mensalidade deve ser maior que zero.")
        self.__mensalidade = valor

    def matricular(self, novo_curso):
        """Matricula o aluno em outro curso (método próprio)."""
        self.__curso = novo_curso
        return f"{self.nome} matriculado em {novo_curso}."

    def calcular_valor_mensal(self):
        """Sobrescreve o método da base: aluno paga a mensalidade."""
        return self.__mensalidade

    def __str__(self):
        """Retorna os dados do aluno."""
        return f"[Aluno] {super().__str__()} | Curso: {self.__curso}"