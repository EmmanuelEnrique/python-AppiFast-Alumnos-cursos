from fastapi import APIRouter, Response, status, Body
from config.db import conn
from schemas.curso import cursoEntity, cursosEntity
from schemas.alumno import alumnoEntity, alumnosEntity
from models.curso import Curso
from models.alumno import Alumno
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

curso = APIRouter()

@curso.get('/cursos/alumnos', response_model=list[Curso], tags=["cursos & alumnos"])
def find_all_curso():
    return cursosEntity(conn.AppiAlumnos.cursos.find())

@curso.get('/cursos', response_model=list[Curso], tags=["cursos"])
def find_all_curso():
    return cursosEntity(conn.AppiAlumnos.cursos.find())


@curso.post('/cursos', response_model=Curso, tags=["cursos"])
def create_curso(curso: Curso):
    new_curso = dict(curso)
    del new_curso["id"]

    id = conn.AppiAlumnos.cursos.insert_one(new_curso).inserted_id
    curso = conn.AppiAlumnos.cursos.find_one({"_id": (id)})
    return cursoEntity(curso)

@curso.get('/cursos/{id}', response_model=Curso, tags=["cursos"])
def find_alumno(id: str):
    return cursoEntity(conn.AppiAlumnos.cursos.find_one({"_id": ObjectId(id)}))


@curso.put('/cursos/{id}', response_model= Curso, tags=["cursos"])
def update_curso(id: str, curso: Curso):
    conn.AppiAlumnos.cursos.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(curso)})

    
@curso.delete('/cursos/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["cursos"])
def delete_curso(id: str):
    cursoEntity(conn.AppiAlumnos.cursos.find_one_and_delete(
        {"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

    
@curso.get('/cursos/alumnos', response_model=list[Curso], tags=["cursos & alumnos"])
def find_all_curso():
    return cursosEntity(conn.AppiAlumnos.cursos.find())



