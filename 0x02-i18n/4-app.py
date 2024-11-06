#!/usr/bin/env python3
"""
This script creates a get_locale function with a
babel.localeselector decorator
"""

from flask_babel import _
from flask import request, render_template
from typing import Optional

Config = __import__('1-app').Config
app = __import__('0-app').app
babel = __import__('1-app').babel


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Optional[str]:
    """This function determines the best match for
    supported languages.
    """
    # Rerieving the value of the locale parameter
    locale_value = request.args.get('locale')

    # Checking if the value exists in the list of languages
    if locale_value in Config.LANGUAGES:
        return locale_value

    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def home() -> str:
    """Rendering the homepage with the
    translated languages.
    """
    return render_template('4-index.html')
