from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.questions_schemas import QuestionsRequest, QuestionResponse
from app.core.db.db import get_async_session
from app.services.question_service import question_service


router = APIRouter(prefix="/questions", tags=["Questions"])


@router.post(
    "/",
    status_code=HTTPStatus.OK,
    response_model=List[QuestionResponse],
    response_model_exclude_none=True,
    summary="Get new questions"
)
async def get_questions(
        request: QuestionsRequest,
        session: AsyncSession = Depends(get_async_session)
) -> List[QuestionResponse]:
    """Get new quiz questions from remote server.

    - **questions_num**: number of questions to be asked.
    """
    result = await question_service.get_and_save_questions(request.questions_num, session)
    return result
