import os
from contextlib import asynccontextmanager
from typing import Annotated

import requests
from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from db_connection import db_create_all, get_db
from model import Note
from schema import CreateNote
import os
from dotenv import load_dotenv
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_create_all()
    print("Creating/Updating db tables")
    print(f'Current env is {os.environ.get("ENVIRONMENT")}')
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
def hello():
    return {"message": "hello I am testserviceb"}


@app.get("/get_testservice")
def get_testservice():
    r = requests.get('http://testservicea.default.svc.cluster.local/hello')
    return r.json()