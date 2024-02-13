from fastapi import FastAPI
from routes.alumno import alumno
from routes.curso import curso

app = FastAPI(
        title= "REST API with FastAPI and Mongodb EEDR",
        description= "This is a simlple REST API using fast and mongodb",
        version="0.0.1"
)

app.include_router(alumno)
app.include_router(curso)


