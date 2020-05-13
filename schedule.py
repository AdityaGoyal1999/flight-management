from flask import Flask, render_template, request

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__, template_folder='templates')

table_name = 'active_flights'
engine = create_engine("postgres://wmbcvvjiskfgau:e516ae997a2f8dfb1c29941e8fab818b76d17672865106f090328c7f5ad4d414@ec2-50-17-21-170.compute-1.amazonaws.com:5432/d3c33hv0lpcnck")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():

    flights = db.execute("SELECT * FROM active_flights").fetchall()
    return render_template("flights.html", flights=flights)
