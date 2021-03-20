import mariadb


config = {
    'host' : 'localhost',
    'port' : 4306,
    'user' : 'root',
    'password' : '1234',
    'database' : 'flask_crud',
}

DB = mariadb.connect(**config)
DB.autocommit = True