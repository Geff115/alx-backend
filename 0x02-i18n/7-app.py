#!/usr/bin/env python3
"""
This script defines a get_timezone function and
uses babel.timezoneselector.
"""

import pytz
from flask import request, g
from typing import Optional
from pytz import exceptions


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
            pass # Go on to the next steps

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
def user_timezone() -> str:
    """Rendering the homepage with the
    translated languages.
    """
    return render_template('7-index.html')