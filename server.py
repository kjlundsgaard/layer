"""Dress for the Weather App"""
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


@app.route('/')
def index():
    """Homepage/Shows user their lists of restaurants"""

    weather_info = weather.get_weather_data(37.7749, 122.4194)

    temp = weather_info['temp']
    humidity = weather_info['humidity']

    return render_template('home.html', temp=temp, humidity=humidity)
##############################################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()
