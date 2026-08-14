-- =====================================================
-- Script de Semeadura (Seed) - Open Boxe
-- =====================================================
-- Execute este script APÓS o script de estrutura.sql

-- =====================================================
-- Usuários Administrativos
-- =====================================================
-- Senha: "senha123" hash com SHA256
-- Em produção, use bcrypt ou argon2
INSERT INTO usuarios (nome, email, nome_usuario, senha) VALUES
('Carlos Silva', 'carlos.silva@openboxe.com', 'carlos_admin', '55a5e9e78207b4df8699d60886fa070079463547b095d1a05bc719bb4e6cd251'),
('Maria Santos', 'maria.santos@openboxe.com', 'maria_admin', '55a5e9e78207b4df8699d60886fa070079463547b095d1a05bc719bb4e6cd251'),
('Pedro Oliveira', 'pedro.oliveira@openboxe.com', 'pedro_admin', '55a5e9e78207b4df8699d60886fa070079463547b095d1a05bc719bb4e6cd251');

-- =====================================================
-- Planos
-- =====================================================
INSERT INTO planos (nome, preco, duracao_meses) VALUES
('Plano Básico', 99.90, 1),
('Plano Intermediário', 149.90, 3),
('Plano Avançado', 199.90, 6),
('Plano Premium', 299.90, 12);

-- =====================================================
-- Treinadores
-- =====================================================
INSERT INTO treinadores (nome, especialidade, biografia) VALUES
('Everton Lopes', 'Boxe Olímpico', 'Campeão mundial amador com mais de 20 anos de experiência em treinamento de alto rendimento.'),
('Ana Ferreira', 'Muay Thai', 'Ex-campeã nacional de Muay Thai, especialista em técnicas de combate corpo a corpo.'),
('Roberto Silva', 'Boxe Profissional', 'Treinador de lutadores profissionais, com experiência em campeonatos nacionais e internacionais.'),
('Juliana Costa', 'Fitness e Condicionamento', 'Especialista em preparação física para atletas de combate, com foco em resistência e força.');

-- =====================================================
-- Alunos
-- =====================================================
INSERT INTO alunos (plano_id, nome, email, data_nascimento) VALUES
(1, 'Lucas Mendes', 'lucas.mendes@email.com', '1995-04-12'),
(1, 'Fernanda Oliveira', 'fernanda.oliveira@email.com', '1998-07-23'),
(2, 'Rafael Souza', 'rafael.souza@email.com', '1992-11-05'),
(2, 'Camila Lima', 'camila.lima@email.com', '1999-02-14'),
(3, 'Gabriel Santos', 'gabriel.santos@email.com', '1990-08-30'),
(3, 'Isabela Ferreira', 'isabela.ferreira@email.com', '1997-06-18'),
(4, 'Thiago Almeida', 'thiago.almeida@email.com', '1988-12-25'),
(4, 'Patrícia Ribeiro', 'patricia.ribeiro@email.com', '1996-03-09'),
(1, 'Diego Castro', 'diego.castro@email.com', '1993-09-17'),
(2, 'Amanda Nascimento', 'amanda.nascimento@email.com', '2000-01-30');

-- =====================================================
-- Atletas (promovidos de alguns alunos)
-- =====================================================
INSERT INTO atletas (aluno_id, categoria_peso, vitorias, derrotas) VALUES
(1, 'Peso Leve', 5, 2),
(3, 'Peso Médio', 8, 1),
(5, 'Peso Pesado', 12, 3),
(7, 'Peso Meio-Médio', 6, 0);

-- =====================================================
-- Turmas
-- =====================================================
INSERT INTO turmas (treinador_id, nome, horario, capacidade) VALUES
(1, 'Boxe Olímpico - Manhã', '07:00 - 08:30', 15),
(1, 'Boxe Olímpico - Noite', '19:00 - 20:30', 15),
(2, 'Muay Thai - Tarde', '14:00 - 15:30', 12),
(3, 'Boxe Profissional - Manhã', '06:00 - 08:00', 10),
(3, 'Boxe Profissional - Noite', '20:00 - 22:00', 10),
(4, 'Condicionamento Físico - Manhã', '08:00 - 09:00', 20),
(4, 'Condicionamento Físico - Tarde', '16:00 - 17:00', 20);

-- =====================================================
-- Validação dos dados inseridos
-- =====================================================
SELECT CONCAT('Usuários cadastrados: ', COUNT(*)) FROM usuarios;
SELECT CONCAT('Planos cadastrados: ', COUNT(*)) FROM planos;
SELECT CONCAT('Treinadores cadastrados: ', COUNT(*)) FROM treinadores;
SELECT CONCAT('Alunos cadastrados: ', COUNT(*)) FROM alunos;
SELECT CONCAT('Atletas cadastrados: ', COUNT(*)) FROM atletas;
SELECT CONCAT('Turmas cadastradas: ', COUNT(*)) FROM turmas;