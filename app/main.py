from threading import Thread

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def index():
    return {'message': 'Welcome to Questions collector API'}


@app.post('/questions', status_code=201, response_model=schemas.Questions | None)
async def download_questions(num: schemas.QuestionsNum, db: Session = Depends(get_db)):
    last_question = crud.get_last_question(db)

    # download in a separate thread to give faster results
    thread = Thread(target=crud.download_new_questions, args=(num.questions_num, db))
    thread.start()

    return last_question
