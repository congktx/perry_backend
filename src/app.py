from flask import Flask
from routes.auth_routes import auth_routes

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.register_blueprint(auth_routes, url_prefix='/api/auth')
    app.run(debug=True, port=2802)
