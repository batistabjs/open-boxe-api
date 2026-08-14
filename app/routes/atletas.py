from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers import ControladorAtletas
from app.models.schemas import AtletaRequest, AtletaResponse
from app.middleware import obter_usuario_atual

router = APIRouter(prefix="/api/v1", tags=["atletas"])

@router.post("/atletas", response_model=AtletaResponse, status_code=201)
def promover_aluno_a_atleta(
    dados: AtletaRequest,
    db: Session = Depends(get_db),
    usuario_atual = Depends(obter_usuario_atual)
):
    controlador = ControladorAtletas(db)
    return controlador.promover_aluno_a_atleta(dados)