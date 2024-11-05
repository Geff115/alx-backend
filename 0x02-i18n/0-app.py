#!/usr/bin/env python3
"""
This script creates a simple Flask app
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """rendering index.html page"""
    return render_template("index.html")
