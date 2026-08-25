from flask import Flask
from database.connection import db
import os
from dotenv import load_dotenv
load_dotenv()
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=(
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT','3306')}/"
    f"{os.getenv('DB_DATABASE')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)
if __name__=='__main__':
    app.run(debug=True)