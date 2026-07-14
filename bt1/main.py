from fastapi import FastAPI
from database import *
import model

app = FastAPI()

Base.metadata.create_all(bind = engine)