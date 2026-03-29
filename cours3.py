from fastapi import FastAPI

app = FastAPI()

@app.get("/candidats/{id}")

def ma_fonction(id):

    ma_liste = [{"id": "1", "nom": "abdel", "metier": "developpeur"},
                {"id": "2", "nom": "eloise", "metier": "ingenieur"}
                ]

    for liste in ma_liste:
        if id == liste["id"] :
            return liste