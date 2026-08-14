from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers import ControladorAlunos
from app.models.schemas import ListagemAlunosResponse
from app.middleware import obter_usuario_atual

router = APIRouter(prefix="/api/v1", tags=["alunos"])

@router.get("/alunos", response_model=ListagemAlunosResponse)
def listar_alunos(
    pagina: int = Query(1, ge=1),
    tamanho_pagina: int = Query(10, ge=1, le=100),
    ordenar_por: str = Query("nome"),
    direcao_ordenacao: str = Query("asc", pattern="^(asc|desc)$"),
    db: Session = Depends(get_db),
    usuario_atual = Depends(obter_usuario_atual)
):
    controlador = ControladorAlunos(db)
    return controlador.listar_alunos(
        pagina=pagina,
        tamanho_pagina=tamanho_pagina,
        ordenar_por=ordenar_por,
        direcao_ordenacao=direcao_ordenacao
    )