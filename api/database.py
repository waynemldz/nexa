from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config.settings import settings

engine = create_engine(settings.DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

# IMPORTAR OS MODELOS SOMENTE DEPOIS DE CRIAR O BASE
from app.models.user import Usuario
from app.models.conversation_state import ConversationState
from app.models.message import Message

Base.metadata.create_all(bind=engine)