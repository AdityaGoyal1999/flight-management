from flask import Flask, render_template, request

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__, template_folder='templates')

table_name = 'active_flights'
engine = create_engine("postgres://wmbcvvjiskfgau:e516ae997a2f8dfb1c29941e8fab818b76d17672865106f090328c7f5ad4d414@ec2-50-17-21-170.compute-1.amazonaws.com:5432/d3c33hv0lpcnck")
db = scoped_session(sessionmaker(bind=engine))
flights = db.execute("SELECT * FROM active_flights").fetchall()

@app.route("/")
def index():

    return render_template("flights.html", flights=flights)

@app.route("/book")
def book():
    return render_template("booking.html", flights=flights)

@app.route("/complete_booking", methods=["POST"])
def complete_booking():
    origin = request.method.get("flight_origin")
    destination = request.method.get("flight_destination")

    print(origin, destination, "PRINTED")

