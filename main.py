from fastapi import FastAPI
from db.database import engine
from db.models import Base
from routers import documents
import uvicorn


# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(documents.router, prefix="/api", tags=["documents"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
