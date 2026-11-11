class Escola:
    """Gerencia a lista de pessoas da escola."""

    def __init__(self, nome):
        """Cria a escola com uma lista vazia de pessoas."""
        self.__nome = nome
        self.__pessoas = []