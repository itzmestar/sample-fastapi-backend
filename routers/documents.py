from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from db import crud, schemas
from db.database import get_db

router = APIRouter()


@router.post("/documents/", response_model=schemas.DocumentRead)
def create_document(document: schemas.DocumentCreate, db: Session = Depends(get_db)):
    # search for document first
    _document = crud.get_document(db, document_id=document.type)
    if _document is None:
        # create the document
        return crud.create_document(db=db, document=document)
    else:
        # update the document with position
        return crud.update_document(db=db, document=document)


@router.get("/documents/", response_model=List[schemas.DocumentRead])
def read_documents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    documents = crud.get_documents(db, skip=skip, limit=limit)
    return documents


@router.get("/documents/{document_id}", response_model=schemas.DocumentRead)
def read_document(document_id: str, db: Session = Depends(get_db)):
    document = crud.get_document(db, document_id=document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document
