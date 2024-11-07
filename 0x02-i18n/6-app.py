#!/usr/bin/env python3
"""
This script updates the get_locale function to use
a user's preferred locale if it is supported.
"""

from flask_babel import gettext
from flask import request, render_template, g
from typing import Optional

Config = __import__('1-app').Config
app = __import__('0-app').app
babel = __import__('1-app').babel
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


@babel.localeselector
def get_locale() -> Optional[str]:
    """This function determines the best match for
    supported languages.
    """
    # Rerieving the value of the locale parameter from the URL
    locale_value = request.args.get('locale')

    if locale_value:
        if locale_value in Config.LANGUAGES:
            return locale_value
    elif g.user:
        # Checking if the user locale is supported
        if g.user['locale'] in Config.LANGUAGES:
            return g.user['locale']
    # Fall back to the best match based on request header
    else:
        return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def user() -> str:
    """Rendering the homepage with the
    translated languages.
    """
    return render_template('6-index.html')
