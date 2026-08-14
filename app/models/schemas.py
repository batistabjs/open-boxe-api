from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from decimal import Decimal

# Schemas para Autenticação
class CadastroRequest(BaseModel):
    nome: str = Field(..., min_length=1)
    email: EmailStr
    nome_usuario: str = Field(..., min_length=1)
    senha: str = Field(..., min_length=6)

class CadastroResponse(BaseModel):
    token_gerado: str
    mensagem: str

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str

class LoginResponse(BaseModel):
    token_gerado: str

class ErroResponse(BaseModel):
    mensagem: str
    erros: Optional[dict] = None

# Schemas para Alunos
class AlunoResponse(BaseModel):
    id: int
    plano_id: int
    nome: str
    email: str
    data_nascimento: str

class ListagemAlunosResponse(BaseModel):
    pagina_atual: int
    tamanho_pagina: int
    total_registros: int
    dados: List[AlunoResponse]

# Schemas para Atletas
class AtletaRequest(BaseModel):
    aluno_id: int
    categoria_peso: str
    vitorias: int = 0
    derrotas: int = 0

class AtletaResponse(BaseModel):
    mensagem: str

# Schemas para Treinadores
class TreinadorResponse(BaseModel):
    id: int
    nome: str
    especialidade: str
    biografia: str

# Schemas para Turmas
class TurmaResponse(BaseModel):
    id: int
    treinador_id: int
    nome: str
    horario: str
    capacidade: int