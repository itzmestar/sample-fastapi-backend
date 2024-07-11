from sqlalchemy import Column, Integer, String
from db.database import Base


class Document(Base):
    __tablename__ = "documents"

    type = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    position = Column(Integer)
