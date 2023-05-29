from datetime import datetime
from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.questions_schemas import QuestionResponse
from app.core.db.models import Questions
from app.services.aiohhtp_service import async_get


TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


class QuestionService:

    async def get_and_save_questions(
            self,
            questions_num: int,
            session: AsyncSession
    ) -> List[QuestionResponse]:
        """Prepares a list of questions for save into the database
        and returns them."""
        questions_to_save = await self._get_questions(questions_num, session)
        return await self._questions_bulk_save(questions_to_save, session)

    async def _get_questions(
            self,
            num: int,
            session: AsyncSession
    ) -> List[QuestionResponse]:
        """Recursively requests questions from remote server until
        questions num is equal to the num."""
        if num == 0:
            return []
        json_load = await async_get(num)
        loaded_questions = await self._json_to_db_questions(json_load)
        loaded_ids = await self._get_ids_from_json(json_load)
        existing_ids = await self._find_exists_questions_ids(loaded_ids, session)
        questions = await self._remove_existing_questions(loaded_questions, existing_ids)
        return questions + await self._get_questions(len(existing_ids), session)

    async def _get_ids_from_json(self, json_load):
        """Parses json data into  a list of ids."""
        return [obj['id'] for obj in json_load]

    async def _json_to_db_questions(
            self,
            json_data: dict
    ) -> List[QuestionResponse]:
        """Parses json data into a list of db Question models."""
        return [
            QuestionResponse(
                id=obj['id'],
                question=obj['question'],
                answer=obj['answer'],
                created_at=datetime.strptime(obj['created_at'], TIME_FORMAT),
                updated_at=datetime.strptime(obj['updated_at'], TIME_FORMAT),
                category=obj['category']['title'],
            ) for obj in json_data
        ]

    async def _find_exists_questions_ids(
            self,
            question_ids: List[int],
            session: AsyncSession
    ) -> List[int]:
        """Returns ids of questions, that already exist."""
        ids = await session.execute(
            select(Questions.id).where(Questions.id.in_(question_ids))
        )
        return ids.scalars().fetchall()

    async def _remove_existing_questions(
        self,
        questions: List[QuestionResponse],
        ids: List[int]
    ) -> List[QuestionResponse]:
        """Removes questions from loaded questions if they already exist."""
        return [question for question in questions if question.id not in ids]

    async def _questions_bulk_save(
            self,
            questions: List[QuestionResponse],
            session: AsyncSession
    ) -> List[QuestionResponse]:
        """Saves questions into the database."""
        questions_to_save = [
            Questions(
                id=question.id,
                question=question.question,
                answer=question.answer,
                category=question.category,
                created_at=question.created_at,
                updated_at=question.updated_at
            ) for question in questions
        ]
        session.add_all(questions_to_save)
        await session.commit()
        return questions


question_service = QuestionService()
