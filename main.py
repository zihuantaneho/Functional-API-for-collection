# головна точка входу
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from db import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/collections/", response_model=schemas.Collection)
def creqate_collection(collection: schemas.CollectionCreate, db: Session = Depends(get_db)):
    return crud.create_collection(db, collection)
@app.get("/collections/", response_model=list[schemas.Collection])
def list_collections(db: Session = Depends(get_db)):
    return crud.get_collection(db)
    
@app.get("/collections/{collection_id}", response_model=schemas.Collection)
def read_collection(collection_id: int, db: Session = Depends(get_db)):
    db_collection = crud.get_collection(db, collection_id)
    if not db_collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    return db_collection
    
@app.post("/collections/{collection_id}/contributions/", response_model=schemas.Contribution)
def add_contribution(collection_id: int, contribution: schemas.ContributionCreate, db: Session = Depends(get_db)):
    return crud.create_contribution(db, collection_id, contribution)
    
@app.get("/collections/underfunded/", response_model=list[schemas.Collection])
def get_underfunded_collections(db: Session = Depends(get_db)):
    return crud.get_underfunded_collections(db)
    