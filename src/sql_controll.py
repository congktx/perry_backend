import mysql.connector
from config import Config

con = mysql.connector.connect(
    host = Config.sql_host,
    user = Config.sql_user,
    password = Config.sql_password,
    database = Config.sql_database
)
