#!/usr/bin/env python3
"""
This script creates a simple Flask app
"""

from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """rendering home page page"""
    return render_template("index.html")
