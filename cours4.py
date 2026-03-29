import psycopg2
from fastapi import HTTPException

def connexion_db():
    conn = None

    try:

        conn = psycopg2.connect(host="ishak", user="ishakuser", password="ishak2301", dbname="ma_db")

        cursor = conn.cursor()

        query_ = "SELECT * FROM candidats"

        cursor.execute(query_)
        resultat = cursor.fetchall()
        return resultat
    except Exception:
        raise HTTPException(status_code=500)

    finally:
        if conn:
            conn.close()


from fastapi import FastAPI

app = FastAPI()

@app.get("/candidats")

def ma_route():

    resultat = connexion_db()

    return resultat

