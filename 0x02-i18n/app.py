#!/usr/bin/env python3
"""
This script determines the current datetime and
based on the inferred timezone and display the
current time on the homepage in the default format
"""


import pytz
from flask_babel import gettext
from flask import request, g, render_template
from typing import Optional
from pytz import exceptions
from datetime import datetime


babel = __import__('1-app').babel
app = __import__('0-app').app
Config = __import__('1-app').Config
get_user = __import__('5-app').get_user
# Importing the users dictionary
users = __import__('5-app').users


app.config.from_object(Config)


@app.before_request
def before_request() -> None:
    """This function uses get_user to find a user
    if any and set it as a global on flask.g.user
    """
    # Get login_as from URL parameter
    login_as = request.args.get("login_as", type=int)
    # Set g.user based on the login_as value
    g.user = get_user(login_as)
    g.timezone = get_timezone()


@babel.timezoneselector
def get_timezone() -> Optional[str]:
    """
    This function determines the best match for timezones
    """
    # Check for timezone in URL parameters
    timezone_value = request.args.get('timezone')

    if timezone_value:
        try:
            # Validating the timezone
            pytz.timezone(timezone_value)
            return timezone_value
        # Invalid timezone error
        except exceptions.UnknownTimezoneError:
            pass  # Go on to the next steps

    # Checking if the user has a preferred timezone
    if g.user and g.user.get('timezone'):
        try:
            # Validate the user's timezone
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except exceptions.UnknownTimezoneError:
            pass

    # Return the default UTC timezone
    return 'UTC'


@app.route('/')
def display_current_time():
    """
    Displaying the current time in the home page
    """
    # Setting the current time based on the selected timezone
    timezone = pytz.timezone(g.timezone or 'UTC')
    current_time = datetime.now(timezone).strftime('%b %d, %Y, %I:%M:%S %p')

    return render_template('index.html', current_time=current_time)
