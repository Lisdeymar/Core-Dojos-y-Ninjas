#necesitamos la conexion a BD, lo mismo del modelo usuarios

from usuarios_app.config.mysqlconnection import connectToMySQL
from usuarios_app.modelos.modelo_ninjas import Ninja


class Dojo:
    def __init__( self, id, name, created_at, updated_at ):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.ninjas = [] #tercer campo inicialmente como un arreglo vacío #ninjas
    
    def agregaUsuario( self, ninja ):
        self.ninjas.append( ninja )

    #RUTA 1A
    @classmethod #controlador ruta 1a para registro
    def agregaDojo( cls, nuevoDojo ): #diccionario creado
        query = "INSERT INTO dojos(name) VALUES(%(name)s)"
        resultado= connectToMySQL( "dojosninjas_schema" ).query_db( query, nuevoDojo )
        return resultado #se lo vamos a devolver al controlador

    #RUTA 1B
    @classmethod
    def obtenerListaDojos( cls):
        query = "SELECT * FROM dojos;"
        resultado = connectToMySQL( "dojosninjas_schema" ).query_db( query )
        listaDojos = []
        for dojo in resultado:
            listaDojos.append( cls( dojo["id"], dojo["name"], dojo["created_at"], dojo["updated_at"])) #Colocar sí o sí todos los atributos que están en el constructor para que funcione
        return listaDojos


    #Ruta 1B ID a RUTA 3A
    @classmethod
    def obtenerDojoConNinjas( cls, dojo ):
        query = "SELECT * FROM dojos d LEFT JOIN ninjas n ON d.id = n.dojo_id WHERE d.id = %(id)s;"
        resultado = connectToMySQL( "dojosninjas_schema" ).query_db( query, dojo )
        print(resultado, "Resultado de obtenerDojosConNinjas" )
        return resultado

