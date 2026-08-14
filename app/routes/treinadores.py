from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers import ControladorTreinadores
from app.models.schemas import TreinadorResponse
from app.middleware import obter_usuario_atual

router = APIRouter(prefix="/api/v1", tags=["treinadores"])

@router.get("/treinadores/{treinador_id}", response_model=TreinadorResponse)
def obter_treinador(
    treinador_id: int,
    db: Session = Depends(get_db),
    usuario_atual = Depends(obter_usuario_atual)
):
    controlador = ControladorTreinadores(db)
    return controlador.obter_treinador_por_id(treinador_id)