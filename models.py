from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Projeto(Base):
    __tablename__ = 'projeto'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    stack = Column(String(100))
    repo_url = Column(String(255))
    criado_em = Column(DateTime, server_default=func.now())