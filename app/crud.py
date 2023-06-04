import requests
from sqlalchemy.orm import Session

from app.models import Question


def download_new_questions(num: int, db: Session) -> None:
    while num:
        result = requests.get(f'https://jservice.io/api/random?count={num}')

        for question in result.json():
            if not db.query(Question).filter(Question.jservice_id == question['id']).first():
                question = Question(jservice_id=question['id'],
                                    question=question['question'],
                                    answer=question['answer'],
                                    jservice_date=question['created_at'])
                db.add(question)
                num -= 1
    db.commit()


def get_last_question(db: Session) -> Question:
    last_question = db.query(Question).order_by(Question.id.desc()).first()
    return last_question
