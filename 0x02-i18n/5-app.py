#!/usr/bin/env python3
"""
This script will mock a database user table.
Logging in will be mocked by passing login_as as
URL parameter containing the user ID to login as.
"""

from typing import Optional
from flask import g, request
from flask_babel import gettext


app = __import__('0-app').app
babel = __import__('1-app').babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as: Optional[dict]) -> Optional[dict]:
    """
    This function uses a mocked database,
    it acts as a user database.
    """
    if login_as is None or login_as not in users:
        return None

    return users[login_as]


@app.before_request
def before_request() -> None:
    """This function uses get_user to find a user
    if any and set it as a global on flask.g.user
    """
    # Get login_as from URL parameter
    login_as = request.args.get("login_as", type=int)
    # Set g.user based on the login_as value
    g.user = get_user(login_as)


@app.route('/')
def home_index() -> str:
    """rendering home page page"""
    return render_template("5-index.html")
