from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.deps import get_db

app = FastAPI()

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    row = result.fetchone()

    return {
        "database": "connected",
        "result": row[0]
    }