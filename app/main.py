from fastapi import FastAPI
from app.database import engine, Base
from app.routers import task

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the task router
app.include_router(task.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI To-Do List API! - Docker"}
