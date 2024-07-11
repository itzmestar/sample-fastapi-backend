from sqlalchemy import Column, Integer, String
from db.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    title = Column(String, index=True)
    position = Column(Integer)
