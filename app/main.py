from fastapi import FastAPI
from pydantic import BaseModel
from src.train import mask_abusive_words, is_toxic
app = FastAPI(title="Toxic Text Detection API")

class TextIn(BaseModel):
    text: str
    threshold: float

class TextOut(BaseModel):
    original_text: str
    is_toxic: bool
    cleaned_text: str

@app.post("/detect", response_model=TextOut)
async def detect_toxicity(request: TextIn):
    cleaned_text = mask_abusive_words(request.text, request.threshold)
    toxic_flag = is_toxic(request.text, request.threshold)
    return {"original_text": request.text, 
            "is_toxic": toxic_flag,
            "cleaned_text": cleaned_text}