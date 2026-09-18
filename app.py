from database import Database
from models import Paciente, MetaTratamento, Recomendacao


db = Database()

# Buscar paciente
dados_paciente = db.buscar_paciente(1)

paciente = Paciente(
    dados_paciente["id"],
    dados_paciente["nome"],
    dados_paciente["avaliacao_inicial"]
)

print("PACIENTE")
print("Nome:", paciente.nome)
print("Avaliação:", paciente.avaliacao_inicial)


# Buscar metas
dados_metas = db.listar_metas(1)

print("\nMETAS DE TRATAMENTO")

for meta in dados_metas:
    meta_objeto = MetaTratamento(
        meta["numero"],
        meta["descricao"]
    )

    print(meta_objeto.numero, "-", meta_objeto.descricao)


# Buscar recomendações
dados_recomendacoes = db.listar_recomendacoes(1)

print("\nRECOMENDAÇÕES")

for recomendacao in dados_recomendacoes:
    recomendacao_objeto = Recomendacao(
        recomendacao["tipo"],
        recomendacao["titulo"],
        recomendacao["descricao"]
    )

    print(recomendacao_objeto.tipo, "-", recomendacao_objeto.titulo)
    print(recomendacao_objeto.descricao)