from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from flask import jsonify,make_response
from flask_json import json_response
import json
from datetime import datetime

app = Flask(__name__)
mysql = MySQL()


def connect():
    app.config['MYSQL_DATABASE_USER'] = 'emmanuel'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'Emman3l247'
    app.config['MYSQL_DATABASE_DB'] = 'credexweb'
    app.config['MYSQL_DATABASE_HOST'] = '192.168.124.247'
    mysql.init_app(app)


@app.route('/')
def hello_world():
    date = datetime.utcnow()
    return render_template('index.html', date=date)


@app.route('/clientes')
def clientes ():
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre from comfu.clientes limit 20")
    data = cursor.fetchall()
    return render_template('clientes.html', data = data)


@app.route('/clientes/add', methods=['POST', 'GET'])
def nuevoCliente():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('nuevoCliente.html')


@app.route('/articulos')
def articulos():
    return render_template('articulos.html')


@app.route('/articulos/add')
def nuevoArticulo():
    return render_template('nuevoArticulo.html')


@app.route('/ventas')
def ventas():
    connect()
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from comfu.clientes limit 2")
    data = cursor.fetchall()
    return render_template('ventas.html', data = data);
    #return jsonify(data)


@app.route('/ventas/add')
def nuevaVenta():
    return render_template('nuevaVenta.html')


@app.route('/configuracion')
def configuracion():
    return render_template('configuracion.html')


if __name__ == '__main__':
    app.run()


