import mysql.connector


class Database:

    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "SUA_SENHA",
            "database": "clinica"
        }

    def conectar(self):
        return mysql.connector.connect(**self.config)

    def buscar_paciente(self, paciente_id):
        conexao = self.conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM pacientes WHERE id = %s",
            (paciente_id,)
        )

        paciente = cursor.fetchone()

        cursor.close()
        conexao.close()

        return paciente

    def listar_metas(self, paciente_id):
        conexao = self.conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM metas_tratamento WHERE paciente_id = %s",
            (paciente_id,)
        )

        metas = cursor.fetchall()

        cursor.close()
        conexao.close()

        return metas

    def listar_recomendacoes(self, paciente_id):
        conexao = self.conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM recomendacoes WHERE paciente_id = %s",
            (paciente_id,)
        )

        recomendacoes = cursor.fetchall()

        cursor.close()
        conexao.close()

        return recomendacoes
    

    