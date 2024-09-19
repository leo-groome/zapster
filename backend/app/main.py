from fastapi import FastAPI, HTTPException
import motor.motor_asyncio
import os
from dotenv import load_dotenv
from beanie import init_beanie, PydanticObjectId
from app.models import UserDocument, UserCreate, TaskDocument, TaskCreate 
from typing import List 
from passlib.context import CryptContext



load_dotenv()

app = FastAPI()

# Connect to MongoDB
MONGO_URL = os.getenv("DB_URL")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["tasks_db"]  # Change to your preferred database name


# Initialize Beanie models at startup
@app.on_event("startup")
async def init_db():
    await init_beanie(database=db, document_models=[UserDocument, TaskDocument])


@app.get("/test-db")
async def test_db():
    try:
        # Test by listing database names
        dbs = await client.list_database_names()
        return {"message": "Coneccion establecida", "Bases de datos": dbs}
    except Exception as e:
        return {"error": str(e)}

# Create a CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Function to hash a password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Create a new user with a random _id and hashed password
@app.post("/users/", response_model=UserDocument)
async def create_new_user(user: UserCreate):
    try:
        # Hash the user's password before storing
        hashed_password = hash_password(user.hashed_password)
        
        # Create a new UserDocument with the hashed password
        new_user = UserDocument(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password  # Store the hashed password
        )
        
        await new_user.insert()  # Insert into the database
        return new_user  # Return the created user with the automatically generated _id
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Crea un task nuevo relacionado a un usuario
@app.post("/tasks/", response_model=TaskDocument)
async def create_task(task: TaskCreate):
    # Checamos si el usuario existe
    user = await UserDocument.get(task.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Se creo la task que se relaciono con el usu
    task_document = TaskDocument(**task.dict())
    await task_document.insert()
    
    return task_document


@app.get("/users/{user_id}/tasks", response_model=List[TaskDocument])
async def get_tasks_for_user(user_id: PydanticObjectId):
    # Check if the user exists
    user = await UserDocument.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Find all tasks associated with the user
    tasks = await TaskDocument.find(TaskDocument.user_id == user_id).to_list()
    
    # If no tasks found, return an empty list
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this user")
    
    return tasks
