def cursoEntity(item) -> dict:
        return{
               "id": str (item["_id"]),
               "curso": item["curso"],
               "name": item["name"],
               "password": item["password"]
               
        }
def cursosEntity(entity) -> list:
       return[cursoEntity(item) for item in entity]