class Pessoa:
    def __init__(self, nome, idade, profissão, renda):
        self.nome = nome
        self.idade = idade
        self.profissão = profissão
        self.renda = renda

    def __str__(self) -> str:
        return f"""\n{self.nome}:
        \tIdade: {self.idade}
        \tProfissão: {self.profissão}
        \tRenda: {self.renda}
        """
