from fastapi import FastAPI
from typing import Optional
from better_profanity import profanity
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str


def test(item):
    profanity.load_censor_words()
    x = item
    output = profanity.censor(x)
    return {"output":output}

@app.post("/predict/")
async def create_item(item: Item):
    return(test(item.name))
