import psycopg2
from fastapi import HTTPException
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv(".env")

class Candidat(BaseModel):
    nom: str
    metier: str
    ville: str

def connexion_db(candidat: Candidat):
    conn = None
    user = os.getenv("USER")
    host = os.getenv("HOST")
    password_db = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    try:

        conn = psycopg2.connect(host=host, user=user, password=password_db, dbname=db_name)

        cursor = conn.cursor()

        # query_ = "SELECT * FROM candidats"
        sueryinsert = "INSERT INTO candidats (nom, metier, ville) VALUES (%s, %s, %s)"

        cursor.execute(sueryinsert, (candidat.nom, candidat.metier, candidat.ville))
        conn.commit()
        return {"Message": "Candidat ajouté"}
        # resultat = cursor.fetchall()
        # return resultat
    except Exception:
        raise HTTPException(status_code=500)

    finally:
        if conn:
            conn.close()

app = FastAPI()

@app.post("/candidats")

def ma_route(candidat: Candidat):

    resultat = connexion_db(candidat)

    return resultat

