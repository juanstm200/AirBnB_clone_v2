#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def starts_a_Flask():
    """display"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def starts_a_Flask2():
    """display"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def reference_data(text):
    """pass a data and show the data"""
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
