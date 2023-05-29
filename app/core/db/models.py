from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Questions(Base):
    """Questions database model."""
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question = Column(String(2048), nullable=False)
    answer = Column(String(2048), nullable=False)
    category = Column(String(256), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=True)

