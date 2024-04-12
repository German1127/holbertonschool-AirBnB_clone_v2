#!/usr/bin/python3
"""Flask instance"""
from flask import Flask, render_template

app = Flask(__name__)
"""Flask instance"""
app.url_map.strict_slashes = False


@app.route('/')
def display_root():
    """returns a simple string"""
    return "Hello HBNB!"


@app.route('/hbnb')
def display_hbnb():
    """returns HBNB string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Function that returns a C string"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/')
@app.route('/python/<text>')
def display_python(text="is cool"):
    """Function that returns a Python string"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def display_n(n):
    """returns a string only if n is a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def display_n_template(n):
    """Return an html page with value of n"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
