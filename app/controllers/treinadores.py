from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Treinador
from ..models.schemas import TreinadorResponse

class ControladorTreinadores:
    def __init__(self, db: Session):
        self.db = db
    
    def obter_treinador_por_id(self, treinador_id: int) -> TreinadorResponse:
        treinador = self.db.query(Treinador).filter(Treinador.id == treinador_id).first()
        
        if not treinador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Identificador de treinador inválido"
            )
        
        return TreinadorResponse(
            id=treinador.id,
            nome=treinador.nome,
            especialidade=treinador.especialidade,
            biografia=treinador.biografia
        )