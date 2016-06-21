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

    weather = weather.get_weather_data(37.7749, 122.4194)

    return jsonify(weather)

##############################################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = False
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    connect_to_db(app, os.environ.get("DATABASE_URL"))

    # Use the DebugToolbar
    # DebugToolbarExtension(app)
    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
