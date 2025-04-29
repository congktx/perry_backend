from flask import Blueprint, jsonify
from sql_controll import con

users_routes = Blueprint('users_routes', __name__)

@users_routes.route('/', methods=['GET'])
def get_users():
    try:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        cursor.close()
        users = [{"id": row[0], "name": row[1]} for row in rows]  
        return jsonify({"users": users}), 200
    except Exception as e:
        return str(e), 500

@users_routes.route('/create-table', methods=['GET'])
def create_table():
    try:
        cursor = con.cursor()
        cursor.execute("create table users(id int primary key, name varchar(255) not null)")
        return "create table success", 200
    except Exception as e:
        return str(e), 500

@users_routes.route('/drop-table', methods=['GET'])
def drop_table():
    try:
        cursor = con.cursor()
        cursor.execute("drop table users")
        return "drop table success", 200
    except Exception as e:
        return str(e), 500
    