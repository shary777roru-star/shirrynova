from flask import Flask, render_template, request, redirect, url_for
import mysql.connector 
app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",      
    user="root",           
    password="password",   
    database="formulario"  
)

@app.route('/')
@app.route('/index') 
def index():
    return render_template('index.html')

@app.route('/coleccion-nueva')
def coleccion_nueva():
    return render_template('coleccion-nueva.html')

@app.route('/ropa')
def ropa():
    return render_template('ropa.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes-somos.html')

@app.route('/sesion', methods=['GET', 'POST'])
def sesion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        return f'<h1>Sesión iniciada para {nombre}</h1>'
    
    return render_template('sesion.html')


@app.route('/inicio-sesion')
def inicio_sesion():
    return render_template('inicio-sesion.html')

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():

    nombre = request.form['nombre']
    email = request.form['email']
    contrasena = request.form['contrasena']

    return f'<h1>Datos recibidos correctamente</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)