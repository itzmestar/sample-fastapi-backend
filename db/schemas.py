from pydantic import BaseModel


class DocumentBase(BaseModel):
    type: str
    title: str
    position: int


class DocumentCreate(DocumentBase):
    pass


class DocumentRead(DocumentBase):

    class Config:
        orm_mode = True
