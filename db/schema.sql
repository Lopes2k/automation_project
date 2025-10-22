CREATE DATABASE IF NOT EXISTS monitoring;


USE monitoring;


CREATE TABLE IF NOT EXISTS status_servicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_servico VARCHAR(100) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL,
    tempo_resposta_ms INT DEFAULT 0,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);