from beanie import Document, init_beanie, PydanticObjectId
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# User BaseModel for validation
# Model for input (creating a user)
class UserCreate(BaseModel):
    username: str
    email: str
    hashed_password: str

# Model for MongoDB (inherits from User and includes _id automatically)
class UserDocument(Document, UserCreate):
    class Settings:
        collection = "users"

class TaskCreate(BaseModel):
    title: str # Obligarorio
    description: Optional[str] = "None"  # Optional 
    due_date: datetime  # Optional 
    tags: Optional[str] = "None"  # Optional 
    status: str = "Todo"  # Default == "Todo" Obligarorio
    user_id: PydanticObjectId  # Relacion con usuario Obligarorio

class TaskDocument(Document, TaskCreate):
    class Settings:
        collection = "tasks"

# Model for updating task status only
class TaskUpdate(BaseModel):
    status: str
