from usuarios_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self, id, first_name, last_name, age, created_at, updated_at, dojo_id ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.created_at = created_at
        self.updated_at = updated_at
        self.dojo_id = dojo_id

    @classmethod #controlador ruta 1a para registro
    def agregaNinja( cls, nuevoNinja ): #diccionario creado
        query = "INSERT INTO ninjas(dojo_id, first_name, last_name, age) VALUES(%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s)"
        resultado= connectToMySQL( "dojosninjas_schema" ).query_db( query, nuevoNinja )
        return resultado #se lo vamos a devolver al controlador