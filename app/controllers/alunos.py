from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from fastapi import HTTPException, status
from ..models import Aluno
from ..models.schemas import ListagemAlunosResponse, AlunoResponse

class ControladorAlunos:
    def __init__(self, db: Session):
        self.db = db
    
    def listar_alunos(
        self,
        pagina: int = 1,
        tamanho_pagina: int = 10,
        ordenar_por: str = "nome",
        direcao_ordenacao: str = "asc"
    ) -> ListagemAlunosResponse:
        # Construir query
        query = self.db.query(Aluno)
        
        # Aplicar ordenação
        coluna_ordenacao = getattr(Aluno, ordenar_por, Aluno.nome)
        if direcao_ordenacao.lower() == "desc":
            query = query.order_by(desc(coluna_ordenacao))
        else:
            query = query.order_by(asc(coluna_ordenacao))
        
        # Contar total de registros
        total_registros = query.count()
        
        # Aplicar paginação
        offset = (pagina - 1) * tamanho_pagina
        alunos = query.offset(offset).limit(tamanho_pagina).all()
        
        # Converter para schema de resposta
        dados = [
            AlunoResponse(
                id=aluno.id,
                plano_id=aluno.plano_id,
                nome=aluno.nome,
                email=aluno.email,
                data_nascimento=aluno.data_nascimento
            )
            for aluno in alunos
        ]
        
        return ListagemAlunosResponse(
            pagina_atual=pagina,
            tamanho_pagina=tamanho_pagina,
            total_registros=total_registros,
            dados=dados
        )