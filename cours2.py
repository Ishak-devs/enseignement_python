class Candidat:
    def __init__(self, nom, metier, ville):
        self.nom = nom
        self.metier = metier
        self.ville = ville

    def present_toi(self):
        return f"Bonjour, je m'appelle {self.nom} et je suis {self.metier} à {self.ville}"

# mon_objet = Candidat("karim", "développeur", "paris")
# print (mon_objet.present_toi())

class CandidatSenior(Candidat):
    def __init__(self, annees_experiences, nom, metier, ville):
        super().__init__(nom, metier, ville)
        self.annee_experiences = annees_experiences

mon_candidat_senior = CandidatSenior("20", "abdel", "developpeur python", "paris")
print (f"{mon_candidat_senior.nom} possède {mon_candidat_senior.annee_experiences} ans d'experiences")

from fastapi import FastAPI

app = FastAPI()

@app.get("/candidats")

def ma_fonction():

    ma_liste = [{"nom": "abdel", "metier": "developpeur"},
                {"nom": "eloise", "metier": "ingenieur"}
                ]
    return ma_liste