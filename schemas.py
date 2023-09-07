from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id:Optional[int]
    username: str
    nombre: str
    rol:str
    estado: int

    class config: 
        orm_mode = True
