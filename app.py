from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecreto'

@app.route('/')
def inicio():
    profesiones= ['Doctor', 'profesor', 'abogado', 'bombero', 'cirujano']
    return render_template('inicio.html', profesiones=profesiones)

@app.route('/enviar', methods=['POST'])
def enviar():
    session['nombre'] = request.form['nombre']
    session['lugar'] = request.form['lugar']
    session['numero'] = request.form['numero']
    session['comida'] = request.form['comida']
    session['profesion'] = request.form['profesion']

    return redirect(url_for('mostrar'))

@app.route('/mostrar')
def mostrar():
    nombre = session.get('nombre', 'Desconocido')
    lugar = session.get('lugar', 'algún lugar')
    numero = session.get('numero', 'algunos')
    comida = session.get('comida', 'comida')
    profesion = session.get('profesion', 'profesión')

    futuro_bueno = f"Soy el adivino del Dojo, {nombre} tendrá un viaje muy largo dentro de {numero} años a {lugar} y estará el resto de sus días preparando {comida} para todas las personas que quieran. Cambio de profesión y ahora es {profesion}."

    futuro_malo = f"Soy el adivino del Dojo, {nombre} tendrá {numero} años de mala suerte, nunca conocerá {lugar} y jamás volvió a comer {comida}."

    session['destino'] = random.choice([futuro_bueno, futuro_malo])

    return render_template('mostrar.html')

if __name__ == '__main__':
    app.run(debug=True)