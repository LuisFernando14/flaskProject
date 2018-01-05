from flask import Flask, render_template
from flaskext.mysql import MySQL

#app = Flask(__name__)
mysql = MySQL()
def connect(app):
    app.config['MYSQL_DATABASE_USER'] = 'MiOficina'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'jfjdjdf/4hj7ag2td7sf52sF5'
    app.config['MYSQL_DATABASE_DB'] = 'credexweb'
    app.config['MYSQL_DATABASE_HOST'] = '35.163.44.18'
    mysql.init_app(app)