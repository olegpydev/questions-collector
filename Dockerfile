FROM python:3.10-slim

WORKDIR /usr/src/questions
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .env .env
COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]