from flask import Flask, render_template
from flaskext.mysql import MySQL

#app = Flask(__name__)
mysql = MySQL()
def connect(app):
    app.config['MYSQL_DATABASE_USER'] = 'emmanuel'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'Emman3l247'
    app.config['MYSQL_DATABASE_DB'] = 'credexweb'
    app.config['MYSQL_DATABASE_HOST'] = '192.168.124.247'
    mysql.init_app(app)