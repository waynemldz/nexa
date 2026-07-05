from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///database.db")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)


class Usuario(Base):
    __tablename__ = "usuarios"

    user_id = Column(String, primary_key=True)
    nome = Column(String)


Base.metadata.create_all(engine)