FROM python:3.9

WORKDIR /app/build

ENV PYTHONPATH /app/build/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=8000"]
