from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI()

@app.get("/health")
def health():
    return {"message": "OK"}

# Définition des modèles
class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

# Liste en mémoire pour stocker les données
phones_db: List[Phone] = []
# Route POST /phones pour ajouter un téléphone
@app.post("/phones", status_code=201)
def create_phone(phone: Phone):
    phones_db.append(phone)
    return phone

# Route GET /phones pour récupérer la liste de tous les téléphones
@app.get("/phones")
def get_phones():
    return phones_db

# Route GET /phones/{id} pour obtenir un téléphone spécifique par identifier
@app.get("/phones/{id}")
def get_phone(id: str):
    for phone in phones_db:
        if phone.identifier == id:
            return phone
    raise HTTPException(status_code=404, detail="Phone not found")
