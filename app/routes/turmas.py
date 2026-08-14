from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers import ControladorTurmas
from app.models.schemas import TurmaResponse
from app.middleware import obter_usuario_atual

router = APIRouter(prefix="/api/v1", tags=["turmas"])

@router.get("/turmas/{turma_id}", response_model=TurmaResponse)
def obter_turma(
    turma_id: int,
    db: Session = Depends(get_db),
    usuario_atual = Depends(obter_usuario_atual)
):
    controlador = ControladorTurmas(db)
    return controlador.obter_turma_por_id(turma_id)