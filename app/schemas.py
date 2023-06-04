from pydantic import BaseModel, Field
from pydantic.schema import datetime


class QuestionsNum(BaseModel):
    questions_num: int = Field(ge=0, le=100)


class Questions(BaseModel):
    id: int
    jservice_id: int
    question: str
    answer: str
    date: datetime
    jservice_date: datetime

    class Config:
        orm_mode = True
