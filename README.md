# Projeto Integrador - Relatório Clínico

Este exemplo usa:

- Python
- Flask
- Orientação a Objetos
- MySQL
- HTML
- CSS

## 1. Criar o banco

Abra o MySQL Workbench e execute todo o conteúdo de `schema.sql`.

Isso cria:

- banco `clinica`
- tabela `pacientes`
- tabela `metas_tratamento`
- tabela `recomendacoes`
- dados de exemplo

## 2. Instalar as bibliotecas

No terminal, dentro da pasta do projeto:

    pip install -r requirements.txt

## 3. Configurar o MySQL

Abra `database.py` e troque:

    "password": "SUA_SENHA"

pela senha do seu MySQL.

Se seu usuário não for `root`, também altere:

    "user": "root"

## 4. Executar

No terminal:

    python app.py

Depois abra no navegador:

    http://127.0.0.1:5000

## 5. Onde está a Orientação a Objetos?

`models.py` possui as classes:

- Paciente
- MetaTratamento
- Recomendacao

`database.py` possui a classe `Database`, que concentra a comunicação com o banco.

O Flask recebe os dados do banco, transforma os registros em objetos e envia esses objetos para o HTML.

## 6. Fluxo do sistema

MySQL
  ↓
Database
  ↓
objetos Python
  ↓
Flask
  ↓
HTML + CSS
  ↓
tela do Relatório Clínico
