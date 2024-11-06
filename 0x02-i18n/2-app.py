#!/usr/bin/env python3
"""
This script creates a get_locale function with a
babel.localeselector decorator
"""

from flask import request
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
    return request.accept_languages.best_match(Config.LANGUAGES)
