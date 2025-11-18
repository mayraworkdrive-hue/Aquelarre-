from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional
from pydantic import BaseModel
from groq import Groq
import os

app = FastAPI(title="Aquelarre")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base de datos
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    credits: int = 2
    is_vip: bool = False

engine = create_engine("sqlite:///./aquelarre.db")
SQLModel.metadata.create_all(engine)

# IA
client = Groq(api_key=os.getenv("GROQ_API_KEY", "gsk_tuclaveaquí"))

class ReadingRequest(BaseModel):
    email: str
    question: str

@app.post("/reading")
def get_reading(req: ReadingRequest):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.email == req.email)).first()
        if not user:
            user = User(email=req.email)
            session.add(user)
            session.commit()

        if user.credits <= 0 and not user.is_vip:
            raise HTTPException(402, "Sin créditos, bruja")

        if not user.is_vip:
            user.credits -= 1
            session.add(user)
            session.commit()

        prompt = f"Eres Valeria, bruja venezolana de Caracas. Habla con acento caribeño, cálido y misterioso. La bruja {req.email.split('@')[0]} pregunta: {req.question}. Haz una lectura de 3 cartas del tarot y dale un consejo potente."

        chat = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-70b-versatile"
        )
        respuesta = chat.choices[0].message.content
        return {"lectura": respuesta, "creditos": user.credits}
