from flask import Flask
from database.connection import db
from models.patient_model import Patient
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
load_dotenv()
app=Flask(__name__)
password=quote_plus(os.getenv("DB_PASSWORD"))
app.config["SQLALCHEMY_DATABASE_URI"]=(
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:"
    f"{password}@" #escapes @
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT','3306')}/"
    f"{os.getenv('DB_DATABASE')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)
@app.route('/test')
def test():
    patients=db.session.execute(db.select(Patient)).scalars().all()
    return {"count":len(patients)}#{"message":"Conntected"}
if __name__=='__main__':
    app.run(debug=True)