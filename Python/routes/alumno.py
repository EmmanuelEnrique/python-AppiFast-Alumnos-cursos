from fastapi import APIRouter, Response, status, Body
from config.db import conn
from schemas.alumno import alumnoEntity, alumnosEntity
from schemas.curso import cursoEntity, cursosEntity
from models.alumno import Alumno
from models.curso import Curso
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

alumno = APIRouter()

@alumno.get('/alumnos', response_model=list[Alumno], tags=["alumnos"])
def find_all_alumno():
    return alumnosEntity(conn.AppiAlumnos.alumno.find())


@alumno.post('/alumnos', response_model=Alumno, tags=["alumnos"])
def create_alumno(alumno: Alumno):
    new_alumno = dict(alumno)
    del new_alumno["id"]

    id = conn.AppiAlumnos.alumno.insert_one(new_alumno).inserted_id
    alumno = conn.AppiAlumnos.alumno.find_one({"_id": id})
    return alumnoEntity(alumno)



@alumno.get('/alumnos/{id}', response_model=Alumno, tags=["alumnos"])
def find_alumno(id: str):
    return alumnoEntity(conn.AppiAlumnos.alumno.find_one({"_id": ObjectId(id)}))

@alumno.put('/alumnos{id}', response_model= Alumno, tags=["alumnos"])
def update_alumno(id: str, alumno: Alumno):
    conn.AppiAlumnos.alumno.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(alumno)}  
    )

@alumno.delete('/alumnos/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=["alumnos"])
def delete_alumno(id: str):
    alumnoEntity(conn.AppiAlumnos.alumno.find_one_and_delete(
        {"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

@alumno.put('/alumnos/cursos{id}', response_model= Alumno, tags=["alumnos/cursos"])
def update_alumno(id: str, alumno: Alumno):
    conn.AppiAlumnos.alumno.find_one_and_update(
        {"_id": [alumno]},
        {"$set": {"alumno.$[curso]": ["curso"] }},
        { "array_filters": [ {"curso": ["curso"]}], "upsert": "true"}   
    )


 

           
        
    
   