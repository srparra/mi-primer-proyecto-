
# 1 haz que muestre en el navegador “¡Hola desde Flask!”

from flask import Flask

app = Flask(__name__)

@app.route('/') 
def divertido():
    return 'hola flask'


# 2 
    



# 3 Crea un patrón de URL y su función respectiva que manejen los siguientes ejemplos:

@app.route('/bienvenido/python') 

def bienvenidopython ():

   return '<h1>¡Bienvenido a esta ruta python!</h1>' 


@app.route('/bienvenido/miyagi') 

def bienvenidomiyagi ():

   return '<h1>¡Bienvenido a esta ruta miyagi!</h1>' 

@app.route('/bienvenido/taquito') 

def bienvenidotaquito ():

   return '<h1>¡Bienvenido a esta ruta taquito!</h1>'



if __name__ == '__main__':
    app.run(debug=True)



4 # 