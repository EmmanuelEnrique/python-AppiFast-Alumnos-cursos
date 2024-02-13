from typing import  Optional
from pydantic import BaseModel

class Curso(BaseModel):
        id: Optional[str]
        curso: str
        name: str
        password: str
        
     
        
        