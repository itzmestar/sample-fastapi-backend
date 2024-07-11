from fastapi import FastAPI
from db.database import engine
from db.models import Base
from routers import documents
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow any origins, methods, and headers for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow any method
    allow_headers=["*"],  # Allow any headers
)

app.include_router(documents.router, prefix="/api", tags=["documents"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
