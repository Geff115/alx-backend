#!/usr/bin/env python3
"""
This script creates a get_locale function with a
babel.localeselector decorator
"""

from flask_babel import Babel, _
from flask import request, render_template
from typing import Optional

Config = __import__('1-app').Config
app = __import__('0-app').app


babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Optional[str]:
    """This function determines the best match for
    supported languages.
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def home() -> str:
    """Rendering the homepage with the
    translated languages.
    """
    return render_template('3-index.html')
