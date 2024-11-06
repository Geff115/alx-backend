#!/usr/bin/env python3
"""
This script instantiate Babel object in the app,
creating a Config class for the Flask app.
"""

from flask_babel import Babel


app = __import__('0-app').app


babel = Babel(app)


class Config:
    """Configuration class for the Babel instance"""
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
