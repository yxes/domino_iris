#!/usr/bin/env python
from flask import Flask, render_template, request
import os
import requests
import json

# configuration
DEBUG = True
API_KEY = os.environ['DOMINO_API_KEY']
MODEL_ATTRS = [
        'sepal_length',
        'sepal_width',
        'petal_length',
        'petal_width'
]

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASK_SETTINGS', silent=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    result = None
    if request.method == 'POST':
        attributes = []
        for field in MODEL_ATTRS:
            attributes.append(request.form[field])
        result = fetch_score(attributes)
        result = result.json()
        if result is not None:
            print("result:", result['result'])
        return render_template('index.html', fields=MODEL_ATTRS, error=error, result=result)

    return render_template('index.html', fields=MODEL_ATTRS)

# you'll want to have your attributes formatted in the right order
def fetch_score(attributes):
    return requests.post("https://app.dominodatalab.com/v1/SparkIQLabs/helloWorld/endpoint",
                headers = {
                    'X-Domino-Api-Key': API_KEY,
                    'Content-type': 'application/json'
                    },
                json={ "parameters": attributes }
    )

if __name__ == '__main__':
    app.run()

