from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = 'serresiete'

@app.route('/')
def index():
    if 'visitas' not in session:
        session['visitas'] = 0
    if 'reinicios' not in session:
        session['reinicios'] = 0
    
    return render_template('index.html', visitas=session['visitas'], reinicios=session['reinicios'])

@app.route('/increment_visits', methods=['POST'])
def increment_visits():
    if 'visitas' in session:
        session['visitas'] += 2  
    return redirect(url_for('index'))

@app.route('/reset_visits', methods=['POST'])
def reset_visits():
    session['visitas'] = 0
    session['reinicios'] += 1
    return redirect(url_for('index'))

@app.route('/add_number', methods=['POST'])
def add_number():
    if 'visitas' in session:
        numero = int(request.form['numero'])
        session['visitas'] += numero
    return redirect(url_for('index'))

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
