from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
