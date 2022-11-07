import os

from fastapi import FastAPI, Request, HTTPException

from models import zoom_event_table
from schema import ZoomEventCreate

app = FastAPI()

ZOOM_WEBHOOK_AUTHORIZATION_TOKEN = os.environ['ZOOM_WEBHOOK_AUTHORIZATION_TOKEN']


from os import environ

import databases

# берем параметры БД из переменных окружения
DB_USER = environ["POSTGRES_USER"]
DB_PASS = environ["POSTGRES_PASSWORD"]
DB_HOST = environ["POSTGRES_HOST"]
DB_NAME = environ["POSTGRES_DB"]
DB_PORT = environ.get("POSTGRES_PORT", "5432")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
# создаем объект database, который будет использоваться для выполнения запросов
database = databases.Database(SQLALCHEMY_DATABASE_URL)


@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()


@app.post("/webhook/zoom-event/")
async def webhook_zoom_events(
        zoom_event: ZoomEventCreate,
        request: Request,
):
    if request.headers['authorization'] != ZOOM_WEBHOOK_AUTHORIZATION_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

    query = zoom_event_table.insert().values(zoom_event.dict())
    event_id = await database.execute(query)

    return {"event_id": event_id}
