CREATE DATABASE IF NOT EXISTS clinica;
USE clinica;

CREATE TABLE pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    avaliacao_inicial TEXT NOT NULL
);

CREATE TABLE metas_tratamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT NOT NULL,
    numero INT NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
);

CREATE TABLE recomendacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
);

INSERT INTO pacientes (nome, avaliacao_inicial)
VALUES (
    'Paciente exemplo',
    'Paciente apresenta dor fantasma tipo queimação no membro inferior direito após amputação transtibial há 6 meses. Intensidade média de 6/10, com piora noturna e em dias frios.'
);

INSERT INTO metas_tratamento (paciente_id, numero, descricao) VALUES
(1, 1, 'Reduzir nível médio de dor para 3/10 em 90 dias'),
(1, 2, 'Implementar rotina diária de terapia do espelho'),
(1, 3, 'Melhorar qualidade do sono (meta: 6h/noite)'),
(1, 4, 'Retorno gradual às atividades físicas adaptadas');

INSERT INTO recomendacoes (paciente_id, tipo, titulo, descricao) VALUES
(1, 'Exercício', 'Mobilidade de quadril', '3 séries de 10 repetições, 2x/dia'),
(1, 'Terapia', 'Terapia do Espelho', 'Sessões de 15 min pela manhã, foco no membro espelhado'),
(1, 'Sono', 'Sono', 'Higiene do sono: cama apenas para dormir, temperatura ambiente 18-22°C');
