from typing import  Optional
from pydantic import BaseModel, Field

class Alumno(BaseModel):
        id: Optional[str]
        name: str
        #email: str
        password: str
        curso: str
        
