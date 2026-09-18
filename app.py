from flask import Flask, render_template
from database import Database
from models import Paciente, MetaTratamento, Recomendacao

app = Flask(__name__)
db = Database()

@app.route("/")
def inicio():
    # Para o exemplo, usamos o paciente de id 1.
    paciente = db.buscar_paciente(1)
    metas = db.listar_metas(1)
    recomendacoes = db.listar_recomendacoes(1)

    paciente_obj = Paciente(
        paciente["id"],
        paciente["nome"],
        paciente["avaliacao_inicial"]
    )

    metas_obj = [
        MetaTratamento(m["numero"], m["descricao"])
        for m in metas
    ]

    recomendacoes_obj = [
        Recomendacao(r["tipo"], r["titulo"], r["descricao"])
        for r in recomendacoes
    ]

    return render_template(
        "relatorio.html",
        paciente=paciente_obj,
        metas=metas_obj,
        recomendacoes=recomendacoes_obj
    )

if __name__ == "__main__":
    app.run(debug=True)
