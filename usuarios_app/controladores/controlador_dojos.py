from flask import render_template, request, redirect, session
from usuarios_app import app
from usuarios_app.modelos.modelo_dojos import Dojo


#RUTA 1 y 1B, la ruta del index
@app.route( '/', methods=["GET"] )
def despliegaAllDojos():
    listaDojos = Dojo.obtenerListaDojos() #acá llamamos al query y la funcion del modeloDojos "obtenerListaDojos"
    print(listaDojos)
    return render_template( "index.html", listaDojos=listaDojos)


#Ruta 1A POST Registrar, insertas información y click, redirecciona a ruta 2
# "y" Se hace cambios para permitir que el usuario se registre con su departamento
@app.route( '/registrodojo', methods=["POST"] )
def registrarDojo(): #diccionario que se va a mandar al query
    nuevoDojo = {
        "name" : request.form["name"],
    }
    session["name"] = request.form["name"] #lo de la sesion para verificacion
    resultado = Dojo.agregaDojo( nuevoDojo ) 
    print( "Resultado", resultado )
    if resultado == False: 
        return redirect( '/' ) #redireccionamos a 1B para que se muestren los resultados
    else:
        return redirect( '/' ) #redireccionamos a 1B para que se muestren los resultados


#Ruta 1B ID a RUTA 3A renderiza click para mostrar pagina del dojo con sus ninjas
@app.route( '/dojos/<int:id>', methods=["GET"] )
def despliegaDojoShow( id ):
    dojoShow = {
        "id": id
    }
    resultado = Dojo.obtenerDojoConNinjas ( dojoShow )
    dojoConNinjas=resultado
    return render_template( "dojoshow.html", dojoConNinjas=dojoConNinjas )


#Sintaxis dojoshow.html
#{{dojoConNinjas[0]['name']}} Ninjas. Colocamos esta sintaxis porque si solo colocamos dojoConNinjas
# no se puede ya que es un arreglo que contiene diccionarios y por cada diccionario arojará el nombre,
# entoces se repite cada vez, por eso solo iterams en el inidce 0, primer diccionario para sacar el nombre 
# del dojo-