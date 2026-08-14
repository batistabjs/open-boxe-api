from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..models import Usuario
from ..models.schemas import CadastroRequest, CadastroResponse, LoginRequest, LoginResponse
from ..middleware import verificar_senha, gerar_hash_senha, criar_token_dados

class ControladorAutenticacao:
    def __init__(self, db: Session):
        self.db = db
    
    def cadastrar(self, dados: CadastroRequest) -> CadastroResponse:
        # Verificar se email já existe
        usuario_existente = self.db.query(Usuario).filter(Usuario.email == dados.email).first()
        if usuario_existente:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={
                    "mensagem": "Propriedades inválidas",
                    "erros": {"email": ["Este e-mail já está em uso"]}
                }
            )
        
        # Verificar se nome de usuário já existe
        usuario_existente = self.db.query(Usuario).filter(Usuario.nome_usuario == dados.nome_usuario).first()
        if usuario_existente:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={
                    "mensagem": "Propriedades inválidas",
                    "erros": {"nome_usuario": ["Este nome de usuário já está em uso"]}
                }
            )
        
        # Criar novo usuário
        novo_usuario = Usuario(
            nome=dados.nome,
            email=dados.email,
            nome_usuario=dados.nome_usuario,
            senha=gerar_hash_senha(dados.senha)
        )
        
        self.db.add(novo_usuario)
        self.db.commit()
        self.db.refresh(novo_usuario)
        
        # Gerar token
        token = criar_token_dados({"id": novo_usuario.id})
        
        return CadastroResponse(
            token_gerado=token,
            mensagem="Cadastro realizado com sucesso"
        )
    
    def login(self, dados: LoginRequest) -> LoginResponse:
        # Buscar usuário por email
        usuario = self.db.query(Usuario).filter(Usuario.email == dados.email).first()
        
        if not usuario or not verificar_senha(dados.senha, usuario.senha):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="E-mail ou senha inválidos"
            )
        
        # Gerar token
        token = criar_token_dados({"id": usuario.id})
        
        return LoginResponse(token_gerado=token)