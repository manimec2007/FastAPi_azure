from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os

df = pd.read_csv('../data/nlpdata.csv')

def get_businessdata(businessname):
    tmp = df[df.BusinessName == BusinessName]
    tjson = tmp.to_json()
    return tjson
app = FastAPI()


@app.get('/')
def index():
    return "Diversity Model NLP enpoint service"

@app.get('/nlp')
def get_businessinfo(businessname:str):
    return os.getcwd()
