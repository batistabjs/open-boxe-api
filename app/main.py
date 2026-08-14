from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import (
    autenticacao_router,
    alunos_router,
    atletas_router,
    treinadores_router,
    turmas_router
)

# Criar aplicação FastAPI
app = FastAPI(
    title="Open Boxe API",
    description="API RESTful para o centro de treinamento Open Boxe",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(autenticacao_router)
app.include_router(alunos_router)
app.include_router(atletas_router)
app.include_router(treinadores_router)
app.include_router(turmas_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def bem_vindo():
    return {
        "mensagem": "Bem-vindo à API Open Boxe",
        "documentacao": "/docs",
        "versao": "1.0.0"
    }