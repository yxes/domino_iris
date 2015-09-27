# domino_iris
Simple example of using a domino-based website.

## Domino API Key

You'll need to use your own domino inspired api key. First
signup with a free account at [Domino](https://www.dominodatalab.com/)
then signin and go to your account settings 
[Account Settings](https://app.dominodatalab.com/account)
where you will find your own personal API key. Copy it.

To run these commands you'll want to set the environment variable:
DOMINO_API_KEY before they'll work.

```{bash}
export DOMINO_API_KEY=<YOUR API KEY>
```

## Included Files

* cli.sh - shell script example for making domino connection
* flask_iris.py - python script for running a simple website
* templates/ - directory for housing jinja2 templates
* static/ - static files for flask

