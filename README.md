# sample-fastapi-backend

When structuring the FastAPI project, the primary goal was to create a clear and maintainable codebase that leverages SQLite for database storage and SQLAlchemy for ORM functionality. The thought process involved breaking down the application into modular components, making it easier to manage and extend in the future.

The first step was to set up the project directory structure. This involved creating separate directories and files for different aspects of the application, such as database connection management (database.py), data models (models.py), data schemas (schemas.py), database interaction functions (crud.py), and API routes (routers/documents.py). This organization ensures that each file has a single responsibility, making the codebase easier to understand and maintain.

In database.py, the SQLite database connection was configured using SQLAlchemy. The SessionLocal and Base were set up to handle database sessions and model declarations, respectively. This setup allows for easy interaction with the SQLite database throughout the application.

The models.py file defines the data model using SQLAlchemy. The Document class represents the table structure, with columns for type, title, and position. Defining the model this way allows SQLAlchemy to map Python objects to database rows seamlessly.

For data validation and serialization, schemas.py was created using Pydantic. The DocumentBase, DocumentCreate, and DocumentRead classes define the structure of the data that will be sent and received via the API. The Config class within DocumentRead ensures that Pydantic can interact with SQLAlchemy models directly.

The crud.py file contains functions for database operations. These functions encapsulate the logic for creating, reading, and retrieving documents, providing a clean interface for interacting with the database. This separation of concerns helps keep the code modular and easier to test.

The API routes are defined in routers/documents.py. Using FastAPI's dependency injection system, the routes are set up to handle HTTP requests and interact with the database via the CRUD functions. The get_db dependency ensures that a database session is available for each request and is properly closed afterward.

Finally, main.py serves as the entry point for the FastAPI application. It sets up the database tables and includes the document router, ensuring that the API is ready to handle requests when the server starts. Running the application with Uvicorn ensures a fast and efficient ASGI server to handle incoming requests.

Overall, the thought process was to create a well-structured, modular, and maintainable FastAPI application that uses SQLite and SQLAlchemy effectively, following best practices for modern web development.

## How to Run:

1. build docker image:
```commandline
docker build -t fastapi-backend .
```

2. Run docker container:
```commandline
docker run -d --name fastapi-container -p 8000:8000 fastapi-backend
```

3. Check Application:

Access Swagger Docs GUI:
```commandline
http://127.0.0.1:8000/docs
```
