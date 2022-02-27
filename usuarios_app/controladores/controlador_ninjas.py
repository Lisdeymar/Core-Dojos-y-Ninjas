from flask import render_template, request, redirect, session
from usuarios_app import app
from usuarios_app.modelos.modelo_ninjas import Ninja
from usuarios_app.modelos.modelo_dojos import Dojo #importamos Dojo para jalar el nombre de los dojos y utilizarlo en Ruta 2

#RUTA 2, la ruta de ninjas.html
@app.route( '/ninjas', methods=['GET'] )
def despliegaRegistroNinja():
    return render_template( "newninja.html", listaDojos = Dojo.obtenerListaDojos() ) 
#Al importar la clase Dojos para poder recibir el nombre del dojo y almacenarlo con el form,
# llamamos a la segunda funcion de obtenerListaDojos del modelo y controladorDojos, la funcion 
# es un select lo cual permite visualizar todos los dojos registrados en la ruta 1A, hacemo uso
# de la funcion de la caja 1B del otro archivo modeloDojos-


#Ruta 2A POST Registrar, insertas información y click, redirecciona a ruta 2
@app.route( '/registroninja', methods=["POST"] )
def registrarNinja(): #diccionario que se va a mandar al query
    nuevoNinja = {
        "dojo_id" : request.form["dojo_id"],
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"], 
        "age" : request.form["age"]
    }
    session["first_name"] = request.form["first_name"] #lo de la sesion para verificacion
    session["last_name"] = request.form["last_name"] #lo de la sesion para verificacion
    resultado = Ninja.agregaNinja( nuevoNinja )
    print( "Resultado", resultado )
    return redirect( '/ninjas' )