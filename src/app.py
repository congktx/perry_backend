from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_routes

app = Flask(__name__)
CORS(app, origins=["*"])

@app.route('/', methods=['GET'])
def get_home():
    return 'Hello, World!'

@app.route('/', methods=['POST'])
def post_home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.register_blueprint(auth_routes, url_prefix='/api/auth')
    app.run(debug=True, port=2802)
