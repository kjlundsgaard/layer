"""Dress for the Weather App"""
from pyzipcode import ZipCodeDatabase
import os
from jinja2 import StrictUndefined
import psycopg2
from flask import Flask, render_template, redirect, request, flash, session, jsonify
import weather

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "supersecretkey"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

zcdb = ZipCodeDatabase()


@app.route('/zip', methods=["POST"])
def show_zip_form():
    """takes zip code info from user form and returns weather API call based on lat/long"""

    zipcode = int(request.form.get('zip'))

    zipcode = zcdb[zipcode]

    lat = zipcode.latitude
    lng = zipcode.longitude

    weather_info = weather.get_weather_data(lat, lng)

    return render_template('home.html', temp=weather_info['temp'], humidity=weather_info['humidity'])


@app.route('/')
def index():
    """Homepage/Shows user their lists of restaurants"""

    weather_info = weather.get_weather_data(37.7749, 122.4194)

    temp = weather_info['temp']
    humidity = weather_info['humidity']

    return render_template('home.html', temp=temp, humidity=humidity)


@app.route('/weather_results.json', methods=["POST"])
def return_weather_results():
    """sends weather API call and sends weather results to client"""

    lat = float(request.form.get('userLat'))
    lng = float(request.form.get('userLng'))

    weather_info = weather.get_weather_data(lat, lng)
    print weather_info

    return jsonify(weather_info)


##############################################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()
