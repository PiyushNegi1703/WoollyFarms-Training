from pydantic import BaseModel


class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True

class Message(BaseModel):
    name:str
    email:str
    message:str