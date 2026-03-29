from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/candidats/{id}")

def ma_fonction(id):

    ma_liste = [{"id": "1", "nom": "abdel", "metier": "developpeur"},
                {"id": "2", "nom": "eloise", "metier": "ingenieur"}
                ]

    for liste in ma_liste:
        if id == liste["id"] :
            return liste

    raise HTTPException(status_code=404)

from pydantic import BaseModel

class Candidat(BaseModel):
    nom: str
    metier: str
    ville: str

ma_liste = []

@app.post("/candidat_ajouter")


def ajouter_liste_candidat(candidat: Candidat):
    ma_liste.append(candidat)
    return ma_liste
