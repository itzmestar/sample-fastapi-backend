from sqlalchemy.orm import Session
from . import models, schemas


def get_documents(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Document).offset(skip).limit(limit).all()


def get_document(db: Session, document_id: str):
    return db.query(models.Document).filter(models.Document.type == document_id).first()


def create_document(db: Session, document: schemas.DocumentCreate):
    db_document = models.Document(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document
