from sqlalchemy import Column, Integer, String, Text, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from ..database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    nome_usuario = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)

class Plano(Base):
    __tablename__ = "planos"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, unique=True, nullable=False)
    preco = Column(Numeric(10, 2), nullable=False)
    duracao_meses = Column(Integer, nullable=False)
    
    alunos = relationship("Aluno", back_populates="plano")

class Aluno(Base):
    __tablename__ = "alunos"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    plano_id = Column(Integer, ForeignKey("planos.id"), nullable=False)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    data_nascimento = Column(String, nullable=False)
    
    plano = relationship("Plano", back_populates="alunos")
    atleta = relationship("Atleta", back_populates="aluno", uselist=False)

class Atleta(Base):
    __tablename__ = "atletas"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"), unique=True, nullable=False)
    categoria_peso = Column(String, nullable=False)
    vitorias = Column(Integer, default=0)
    derrotas = Column(Integer, default=0)
    
    aluno = relationship("Aluno", back_populates="atleta")

class Treinador(Base):
    __tablename__ = "treinadores"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String, nullable=False)
    biografia = Column(Text, nullable=False)
    
    turmas = relationship("Turma", back_populates="treinador")

class Turma(Base):
    __tablename__ = "turmas"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    treinador_id = Column(Integer, ForeignKey("treinadores.id"), nullable=False)
    nome = Column(String, nullable=False)
    horario = Column(String, nullable=False)
    capacidade = Column(Integer, nullable=False)
    
    treinador = relationship("Treinador", back_populates="turmas")