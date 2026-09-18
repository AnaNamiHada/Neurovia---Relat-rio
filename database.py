import os
import mysql.connector


class Database:
    """Classe responsável pela comunicação com o MySQL."""

    def __init__(self):
        self.config = {
            "host": os.getenv("DB_HOST", "localhost"),
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD", "SUA_SENHA"),
            "database": os.getenv("DB_NAME", "clinica"),
        }

    def conectar(self):
        return mysql.connector.connect(**self.config)

    def buscar_paciente(self, paciente_id):
        conn = self.conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT id, nome, avaliacao_inicial "
            "FROM pacientes WHERE id = %s",
            (paciente_id,)
        )

        paciente = cursor.fetchone()

        cursor.close()
        conn.close()
        return paciente

    def listar_metas(self, paciente_id):
        conn = self.conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT numero, descricao "
            "FROM metas_tratamento "
            "WHERE paciente_id = %s "
            "ORDER BY numero",
            (paciente_id,)
        )

        metas = cursor.fetchall()

        cursor.close()
        conn.close()
        return metas

    def listar_recomendacoes(self, paciente_id):
        conn = self.conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT tipo, titulo, descricao "
            "FROM recomendacoes "
            "WHERE paciente_id = %s "
            "ORDER BY id",
            (paciente_id,)
        )

        recomendacoes = cursor.fetchall()

        cursor.close()
        conn.close()
        return recomendacoes
