from flask import Blueprint, request, jsonify
from flask_cors import CORS
from mongo_controll import Users, Codes
import bcrypt
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from config import Config
import random
from google.oauth2 import id_token
from google.auth.transport import requests

auth_routes = Blueprint('auth_routes', __name__)
CORS(auth_routes, origins=["*"])

@auth_routes.route('/login-gmail', methods=['POST'])
def login_gmail():
    try:
        print(request.json.get('id_token'))
        token = request.json.get('id_token')
        if not token:
            return jsonify({'error': 'Missing ID token'}), 400

        idinfo = id_token.verify_oauth2_token(token, requests.Request(), Config.CLIENT_ID)
        print(idinfo)

        # {'iss': 'https://accounts.google.com', 'azp': '616106247599-e1671q0gghacqbfp99bsq206bc4ovknc.apps.googleusercontent.com', 'aud': '616106247599-e1671q0gghacqbfp99bsq206bc4ovknc.apps.googleusercontent.com', 'sub': '103044462193221315373', 'email': 'buicongvip@gmail.com', 'email_verified': True, 'nbf': 1746529691, 'name': 'Công Bùi Thành', 'picture': 'https://lh3.googleusercontent.com/a/ACg8ocJjrU_CMI40oFbM2dQ-yfeFlj1i0hz3LY7kwsNF8YNSBid9Kcw=s96-c', 'given_name': 'Công', 'family_name': 'Bùi Thành', 'iat': 1746529991, 'exp': 1746533591, 'jti': 'd4acd36fc97715fbe6e8c7eaac5d18beaf99b9ec'}

        return jsonify(idinfo), 200
    except Exception as e:  
        print(e)
        return str(e), 500

# @auth_routes.route('/register', methods=['POST'])
# def register():
#     try:
#         data = request.get_json()
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')

#         existing_user = Users.find_one({'$or':[{'email': email}, {'username': username}]})

#         if (existing_user and existing_user['verified'] == True):
#             return jsonify({"message": "Email or username is already in use, Please login."}), 400
        
#         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#         if existing_user:
#             existing_user['username'] = username
#             existing_user['password'] = hashed_password.decode('utf-8')    
#             existing_user['verified'] = False
#             Users.update_one({'email': email}, {'$set': existing_user})
#         else:
#             new_user = {
#                 'username': username,
#                 'email': email,
#                 'password': hashed_password.decode('utf-8'),
#                 'verified': False
#             }
#             Users.insert_one(new_user)

#         return jsonify({"message": "User registered successfully"}), 200
#     except Exception as e:
#         return str(e), 500
    
# @auth_routes.route('/login', methods=['POST'])
# def login():
#     try:
#         data = request.get_json()
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')

#         user = Users.find_one({'$or':[{'email': email}, {'username': username}]})
#         if not user:
#             return jsonify({"message": "User not found"}), 401

#         if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
#             return jsonify({"message": "Login successful"}), 200
#         else:
#             return jsonify({"message": "Wrong email/username or password"}), 401
#     except Exception as e:
#         return str(e), 500

# @auth_routes.route('/send-verification-email', methods=['POST'])
# def send_verification_email():
#     try:
#         data = request.get_json()
#         email = data.get('email')
#         print(email)

#         if not email:
#             return jsonify({"message": "Email are required"}), 400
        
#         code = random.randint(10**9, 10**10 - 1)  
#         new_code = {
#             'code': code
#         }
#         Codes.insert_one(new_code)

#         message = Mail(
#             from_email=Config.MAILER,  
#             to_emails=email,
#             subject='Email Verification',
#             html_content=f"""
#             <p>Thank you for registering. Please verify your email by clicking the link below:</p>
#             <a href="http://localhost:2802/api/auth/verify-email?email={email}&code={code}">Verify Email</a>
#             """
#         )

#         sg = SendGridAPIClient(Config.SG_KEY)
#         response = sg.send(message)

#         # Check response status
#         if response.status_code == 202:
#             return jsonify({"message": "Verification email sent successfully"}), 200
#         else:
#             return jsonify({"error": f"Failed to send email. Status code: {response.status_code}"}), 500

#     except Exception as e:
#         # Handle exceptions and log the error
#         return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
# @auth_routes.route('/verify-email', methods=['GET'])
# def verify_email():
#     try:
#         email = request.args.get('email')
#         code = request.args.get('code')
#         if not code:
#             return jsonify({"message": "Code is required"}), 400

#         code_entry = Codes.find_one({'code': int(code)})
#         if not code_entry:
#             return jsonify({"message": "Invalid or expired code"}), 400
        
#         Users.find_one_and_update({'email': email}, {'$set': {'verified': True}})
#         Codes.delete_one({'code': int(code)})

#         return jsonify({"message": "Email verified successfully"}), 200
#     except Exception as e:
#         return str(e), 500
