class Paciente:
    def __init__(self, id, nome, avaliacao_inicial):
        self.id = id
        self.nome = nome
        self.avaliacao_inicial = avaliacao_inicial


class MetaTratamento:
    def __init__(self, numero, descricao):
        self.numero = numero
        self.descricao = descricao


class Recomendacao:
    def __init__(self, tipo, titulo, descricao):
        self.tipo = tipo
        self.titulo = titulo
        self.descricao = descricao
