-- =====================================================
-- Script de Criação do Banco de Dados - Open Boxe
-- MySQL / MariaDB
-- =====================================================

-- Criar banco de dados (caso não exista)
CREATE DATABASE IF NOT EXISTS open_boxe
 CHARACTER SET utf8mb4
 COLLATE utf8mb4_unicode_ci;

-- Selecionar banco de dados
USE open_boxe;

-- =====================================================
-- Tabela de Usuários (para autenticação administrativa)
-- =====================================================
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    nome_usuario VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- =====================================================
-- Tabela de Planos
-- =====================================================
CREATE TABLE IF NOT EXISTS planos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) UNIQUE NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    duracao_meses INT NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- =====================================================
-- Tabela de Alunos
-- =====================================================
CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plano_id INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (plano_id) REFERENCES planos(id)
) ENGINE=InnoDB;

-- =====================================================
-- Tabela de Atletas (relacionamento 1:1 com Alunos)
-- =====================================================
CREATE TABLE IF NOT EXISTS atletas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT UNIQUE NOT NULL,
    categoria_peso VARCHAR(100) NOT NULL,
    vitorias INT DEFAULT 0,
    derrotas INT DEFAULT 0,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
) ENGINE=InnoDB;

-- =====================================================
-- Tabela de Treinadores
-- =====================================================
CREATE TABLE IF NOT EXISTS treinadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    especialidade VARCHAR(255) NOT NULL,
    biografia TEXT NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- =====================================================
-- Tabela de Turmas
-- =====================================================
CREATE TABLE IF NOT EXISTS turmas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    treinador_id INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    horario VARCHAR(100) NOT NULL,
    capacidade INT NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (treinador_id) REFERENCES treinadores(id)
) ENGINE=InnoDB;

-- =====================================================
-- Índices para melhor performance
-- =====================================================
CREATE INDEX idx_usuarios_email ON usuarios(email);
CREATE INDEX idx_usuarios_nome_usuario ON usuarios(nome_usuario);
CREATE INDEX idx_alunos_plano_id ON alunos(plano_id);
CREATE INDEX idx_alunos_email ON alunos(email);
CREATE INDEX idx_atletas_aluno_id ON atletas(aluno_id);
CREATE INDEX idx_turmas_treinador_id ON turmas(treinador_id);