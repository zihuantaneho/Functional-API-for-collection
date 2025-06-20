# логіка взаємодії з БД
from sqlalchemy.orm import Session
import models, schemas

def create_collection(db: Session, collection: schemas.CollectionCreate):
    db_collection = models.Collection(**collection.dict())
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)
    return db_collection
def get_collection(db: Session):
    return db.query(models.Collection).all()

def get_collection(db: Session, collection_id: int):
    return db.query(models.Collection).filter(models.Collection.id == collection_id).first()

def create_contribution(db: Session, collection_id: int, contribution: schemas.ContributionCreate):
    db_contribution = models.Contribution(collection_id=collection_id, **contribution.dict())
    db.add(db_contribution)
    db.commit()
    db.refresh(db_contribution)
    return db_contribution

def get_underfunded_collections(db: Session):
    collection = db.query(models.Collection).all()
    return [col for col in collection if sum(c.amount for c in col.contributions) < col.target_amount]

