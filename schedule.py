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
    flights = db.execute("SELECT * FROM active_flights").fetchall()
    return render_template("flights.html", flights=flights)


@app.route("/flights")
def flights():

    flights = db.execute("SELECT * FROM active_flights").fetchall()
    return render_template("flights.html", flights=flights)


@app.route("/flights/<int:id>")
def flight(id):

    flight = db.execute("SELECT * FROM active_flights WHERE id = :id", {"id": id}).fetchone()
    return render_template("flight.html", flight=flight)


@app.route("/booking", methods=["POST", "GET"])
def booking():
    # origin = request.form["flight_origin"]
    # destination = request.form["flight_destination"]

    # message = "Your flight has been booked"
    # try:
    #     db.execute("UPDATE active_flights SET numPassengers = numPassengers + 1 WHERE origin = '{}' AND destination = '{}';".format(origin, destination))
    #     db.commit()
    # except:
    #     message = "There was an error in selecting the flight"
        
    # return render_template("error.html", message=message)
    # return "Works"
    flights = db.execute("SELECT * FROM active_flights;").fetchall()
    return render_template("booking.html", flights=flights)


@app.route("/book", methods=["POST"])
def book():
    origin = request.form["flight_origin"]
    destination = request.form["flight_destination"]
    name = request.form["usersname"]
    date = request.form["date"] # getting in "2020-11-23" format of type string

    # TODO: need to commit these to the database

    return "Your flight has been booked"


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    index()


