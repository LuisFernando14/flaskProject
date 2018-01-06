from flaskext.mysql import MySQL

mysql = MySQL()


class DBConfig():
    app = None
    mysql = MySQL()
    DATABASE_USER = 'apiconcretest'
    DATABASE_PASSWORD = 'ApiConcreT3st'
    DATABASE_DEFAULT_DB = 'credexweb'
    DATABASE_HOST = '52.33.17.144'

    def __init__(self, app):
        self.app = app

    def connect(self):
        self.app.config['MYSQL_DATABASE_USER'] = self.DATABASE_USER
        self.app.config['MYSQL_DATABASE_PASSWORD'] = self.DATABASE_PASSWORD
        self.app.config['MYSQL_DATABASE_DB'] = self.DATABASE_DEFAULT_DB
        self.app.config['MYSQL_DATABASE_HOST'] = self.DATABASE_HOST
        mysql.init_app(self.app)
