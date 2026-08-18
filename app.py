from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__, static_folder='static')


# =====================================================
# CONFIGURACIÓN DE LA BASE DE DATOS
# =====================================================

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mysql',
    'database': 'adopciones_db'
}


# =====================================================
# CONECTAR A LA BASE DE DATOS
# =====================================================

def conectar_bd():
    return mysql.connector.connect(**DB_CONFIG)


# =====================================================
# PÁGINA PRINCIPAL
# =====================================================

@app.route('/')
def inicio():
    return render_template('index.html')


# =====================================================
# REGISTRAR MASCOTA
# =====================================================

@app.route('/registrar', methods=['POST'])
def registrar():

    nombre = request.form.get('nombre', '').strip()
    tipo = request.form.get('tipo', '').strip()
    raza = request.form.get('raza', '').strip()
    edad = request.form.get('edad', '').strip()
    sexo = request.form.get('sexo', '').strip()
    tamano = request.form.get('tamano', '').strip()
    descripcion = request.form.get('descripcion', '').strip()
    ciudad = request.form.get('ciudad', '').strip()

    # Verificar datos obligatorios
    if not nombre or not tipo or not edad:
        return "Error: nombre, tipo y edad son obligatorios."

    conexion = None
    cursor = None

    try:

        conexion = conectar_bd()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO mascotas
            (nombre, tipo, raza, edad, sexo, tamano,
             descripcion, ciudad, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            nombre,
            tipo,
            raza,
            edad,
            sexo,
            tamano,
            descripcion,
            ciudad,
            'Disponible'
        ))

        conexion.commit()

    except mysql.connector.Error as error:

        if conexion:
            conexion.rollback()

        return f"Error al registrar la mascota: {error}"

    finally:

        if cursor:
            cursor.close()

        if conexion:
            conexion.close()

    return redirect(url_for('ver_mascotas'))


# =====================================================
# VER MASCOTAS
# =====================================================

@app.route('/mascotas')
def ver_mascotas():
    conexion = None
    cursor = None
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("""
            SELECT *
            FROM mascotas
            ORDER BY id DESC
        """)
        mascotas = cursor.fetchall()
        
        # Aquí enviamos los datos ordenados a tu archivo html real
        return render_template('usuarios.html', mascotas=mascotas)

    except mysql.connector.Error as error:
        return f"Error al consultar las mascotas: {error}"
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


# =====================================================
# INICIAR APLICACIÓN
# =====================================================
if __name__ == '__main__':
    app.run(debug=True
    )