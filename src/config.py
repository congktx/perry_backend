from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    sql_host = "localhost"
    sql_user = "congktx"
    sql_password = "123"
    sql_database = "mydatabase"
    MONGO_URI = os.getenv("MONGO_URI")
    MAILER=os.getenv("MAILER")
    SG_KEY=os.getenv("SG_KEY")
    CLIENT_ID=os.getenv("CLIENT_ID")