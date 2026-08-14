from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.controllers import ControladorAutenticacao
from app.models.schemas import CadastroRequest, CadastroResponse, LoginRequest, LoginResponse
from app.middleware import obter_usuario_atual

router = APIRouter(prefix="/api/v1/autenticacao", tags=["autenticação"])

@router.post("/cadastro", response_model=CadastroResponse, status_code=201)
def cadastrar(dados: CadastroRequest, db: Session = Depends(get_db)):
    controlador = ControladorAutenticacao(db)
    return controlador.cadastrar(dados)

@router.post("/login", response_model=LoginResponse)
def login(dados: LoginRequest, db: Session = Depends(get_db)):
    controlador = ControladorAutenticacao(db)
    return controlador.login(dados)

@router.delete("/sair", status_code=204)
def sair(usuario_atual = Depends(obter_usuario_atual)):
    # Em uma implementação real, poderíamos adicionar o token a uma blacklist
    # Por simplicidade, apenas retornamos sucesso
    return None