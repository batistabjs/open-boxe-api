from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Aluno, Atleta
from ..models.schemas import AtletaRequest, AtletaResponse

class ControladorAtletas:
    def __init__(self, db: Session):
        self.db = db
    
    def promover_aluno_a_atleta(self, dados: AtletaRequest) -> AtletaResponse:
        # Verificar se o aluno existe
        aluno = self.db.query(Aluno).filter(Aluno.id == dados.aluno_id).first()
        if not aluno:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Identificador de aluno inválido"
            )
        
        # Verificar se o aluno já é atleta
        atleta_existente = self.db.query(Atleta).filter(Atleta.aluno_id == dados.aluno_id).first()
        if atleta_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este aluno já é um atleta"
            )
        
        # Criar novo atleta
        novo_atleta = Atleta(
            aluno_id=dados.aluno_id,
            categoria_peso=dados.categoria_peso,
            vitorias=dados.vitorias,
            derrotas=dados.derrotas
        )
        
        self.db.add(novo_atleta)
        self.db.commit()
        
        return AtletaResponse(mensagem="Registro de atleta criado com sucesso")