from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente

def hola_mundo():
   return render_template('index.html')  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route ('/descripcion')
def testing ():
   return '<h1>pagina de descripcion</h1>'

@app.route('/hola/<nombre>/<apellido>/<int:edad>') # el hola es la nueva ruta no lleva <> , tienes que definir el (hola y agregar el hola apellido y edad ) tambien se puede agregar  
def hola(nombre, apellido,edad):                            #int y mas cositas para aserlo en la forma quieras.
      return (f"<h1>hola {nombre} {apellido} , de {edad}  años<h1>")

@app.route ('/saludo/<nombre>/<int:num>')   
def saludo (nombre,num) : 
    return  (f'¡Hola {nombre}!'*num)

@app.route ('/suma/<int:num1>/int:num2>')
def suma(num1,num2): 
    return (f'{num1} + {num2} = {num1 + num2}')

@app.route('/resta/<int:num1>/<int:num2>')
def resta (num1,num2):
    return (f'{num1} - {num2} = {num1 - num2}')    

#actividad  num4  haz que muestre en el navegador “Repite después de mi: ” y la cadena “hola” 5 veces.

@app.route('/repite5/<nombre>/<int:num>')
def repite5(nombre,num):
    return (f'repite despues de mi:'({nombre}*num ))
# SIEMPRE ESTO TIENE QUE IR ABAJO 

if __name__=="__main__":
   app.run(debug=True)