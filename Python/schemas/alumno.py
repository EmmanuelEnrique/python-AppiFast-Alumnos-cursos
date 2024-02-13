def alumnoEntity(item) -> dict:
        return{
               "id":  str (item["_id"]),
               "name": item["name"],
               #"email": item["email"],
               "password": item["password"],
               "curso": item["curso"]
        }
def alumnosEntity(entity) -> list:
       return[alumnoEntity(item) for item in entity]