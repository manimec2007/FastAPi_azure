from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

df = pd.read_csv('/home/data/nlpdata.csv')

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
    res = get_businessdata(businessname)
    return res
