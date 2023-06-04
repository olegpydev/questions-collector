from pydantic.schema import datetime
from sqlalchemy import TIMESTAMP, Column, Integer, String
from sqlalchemy.sql import func

from .database import Base


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    jservice_id = Column(Integer, unique=True)
    question = Column(String(1000))
    answer = Column(String(100))
    date = Column(TIMESTAMP(timezone=True), server_default=func.now())
    jservice_date = Column(TIMESTAMP(timezone=True))

    def __init__(self, jservice_id: int, question: str, answer: str, jservice_date: datetime):
        self.jservice_id = jservice_id
        self.question = question
        self.answer = answer
        self.jservice_date = jservice_date

    def __repr__(self) -> str:
        return f'<Question: {self.question}>'
