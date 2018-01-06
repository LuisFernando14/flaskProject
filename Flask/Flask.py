# coding=utf-8
from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from flask import jsonify,make_response
from flask_json import json_response
from sqlalchemy import *
import json
from db import DBConfig
from datetime import datetime

app = Flask(__name__)
mysql = MySQL()


def connect():
    dbConfig = DBConfig.DBConfig(app)
    return dbConfig.connect()

@app.route('/')
def hello_world():
    date = datetime.utcnow()
    return render_template('index.html', date=date)


@app.route('/clientes')
def clientes ():
    connect()
    conn = DBConfig.mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, status FROM comfu.tarjetasStpClientes LIMIT 10")
    data = cursor.fetchall()
    return render_template('clientes.html', data = data)


@app.route('/clientes/add', methods=['POST', 'GET'])
def nuevoCliente():
    if request.method == 'POST':
        connect()
        conn = DBConfig.mysql.connect()
        cursor = conn.cursor()
        idBanco = request.form['idBanco']
        idCliente = request.form['idCliente']
        status = request.form['status']
        tarjeta = request.form['tarjeta']
        cursor.execute("INSERT INTO comfu.tarjetasStpClientes(banco, idCliente, status, tarjeta) VALUES (%s,%s,%s,%s)",
                  (idBanco, idCliente, status, tarjeta))
        conn.commit()
        conn.close()
        return redirect('clientes')
    #Debo obtener le último id primero
    connect()
    conn = DBConfig.mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM comfu.tarjetasStpClientes")
    id = cursor.fetchone()
    conn.commit()
    conn.close()
    return render_template('nuevoCliente.html', data=id)

@app.route('/clientes/<idTarjeta>')
def detalleArticulo(idTarjeta):
    connect()
    conn = DBConfig.mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM comfu.tarjetasStpClientes where id = %s", idTarjeta)
    article = cursor.fetchall()
    conn.commit()
    conn.close()
    #return jsonify(art = article)
    app.add_url_rule('/clientes/<idTarjeta>', 'detalleArticulo', detalleArticulo)
    return render_template("detalleArticulo.html", data=article)


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


