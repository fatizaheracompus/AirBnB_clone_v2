#!/usr/bin/python3
"""script that start  Flask web application"""


# import Flask class from flask module
from flask import Flask

# creates instance called app of the class by pass the __name__ variable
appc = Flask(__name__)
appc.url_map.strict_slashes = False


@appc.route('/')
def index():
    """display "Hello HBNB!"

    Return:
        str: texte on the index page
    """
    return 'Hello HBNB!'


@appc.route('/hbnb')
def hbnb_route():
    """displays "HBNB

    Return:
        str: texte on the page
    """
    return 'HBNB'


@appc.route('/c/<text>')
def c_route(text):
    """display "C", follow by the value the text variable

    Args:
        text (str): text to be serve the page

    Return:
        str: texte on the page
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    appc.run(debug=True)