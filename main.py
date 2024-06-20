from fastapi import FastAPI
from database import Base, engine
from api.users_api import users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/', title='Sky bird')

app.include_router(users_router)

