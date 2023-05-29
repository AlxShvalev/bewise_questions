from datetime import datetime

from pydantic import BaseModel, Extra, Field


class QuestionsRequest(BaseModel):
    """Class for creating project request data."""
    questions_num: int = Field()

    class Config:
        extre = Extra.forbid


class QuestionResponse(BaseModel):
    """Class for questions responses."""
    id: int
    question: str
    answer: str
    category: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
