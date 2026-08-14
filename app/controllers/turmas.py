from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Turma
from ..models.schemas import TurmaResponse

class ControladorTurmas:
    def __init__(self, db: Session):
        self.db = db
    
    def obter_turma_por_id(self, turma_id: int) -> TurmaResponse:
        turma = self.db.query(Turma).filter(Turma.id == turma_id).first()
        
        if not turma:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Identificador de turma inválido"
            )
        
        return TurmaResponse(
            id=turma.id,
            treinador_id=turma.treinador_id,
            nome=turma.nome,
            horario=turma.horario,
            capacidade=turma.capacidade
        )