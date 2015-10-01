#!/usr/bin/env python

"""

Author: Stephen D. Wells <wells@cedarnet.org>
Date: 9/31/15
Version: 0.01 - currently no error checking / debug

Runs a simple webserver that passes values from
a form to Domino Data Labs via their API. The 
return value is then sent to the template for
rendering.

"""
# EXTERNAL LIBRARIES

# Flask is our Web Framework in this case
from flask import Flask, render_template, request
import os # grab the ENV variable
import requests # make Domino API Request
import json # parse Domino's results

# CONFIGURATION

# before running this program please ensure
# that you've setup your Domino API Key
# from http://dominodatalab.com/

# export DOMINO_API_KEY='xA3f...Syds'

API_KEY = os.environ['DOMINO_API_KEY']

# This is a list of keys your API requires.
# The order of these variables is important.
# You have been warned.
MODEL_ATTRS = [
    'sepal_length',
    'sepal_width',
    'petal_length',
    'petal_width'
]

# Fire up our Flask Object
app = Flask(__name__)
app.config.from_object(__name__)

# If you'd rather load from a config file...
#   http://flask.pocoo.org/docs/0.10/tutorial/setup/
#app.config.from_envvar('FLASK_SETTINGS', silent=True)

# INDEX PAGE - all the magic happens here
@app.route('/', methods=['GET', 'POST'])
def index():
    error = None # we don't use this... but we should eventually so I left it
    result = None # the json variable we get back from Domino

    if request.method == 'POST': # you submitted the form

        attributes = [] # just the values from the form in an array
        for field in MODEL_ATTRS:
            attributes.append(request.form[field])

        result = fetch_score(attributes)
        result = result.json()

        if result is not None: # notice that we don't do anything if it didn't work
                               # we should eventually - consider this a placeholder
            print("result:", result['result'])

        # since we got a result we pass it to the template for rendering
        #    once again - error is always None at this stage
        return render_template('index.html', fields=MODEL_ATTRS, error=error, result=result)

    # by not returning result it passes to the template as not defined - we can use that!
    return render_template('index.html', fields=MODEL_ATTRS)

# DOMINO API REQUEST

# you'll want to have your attributes formatted in the right order - see above
def fetch_score(attributes):
    return requests.post("https://app.dominodatalab.com/v1/SparkIQLabs/helloWorld/endpoint",
                headers = {
                    'X-Domino-Api-Key': API_KEY,
                    'Content-type': 'application/json'
                    },
                json={ "parameters": attributes }
    )

# START YOUR ENGINES!

# This allows you to use this script as a library instead of an executable
#  which though highly unlikely is good practice...
if __name__ == '__main__':
    app.run()

