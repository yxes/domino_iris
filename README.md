# domino_iris
Simple example of using a domino-based website.

## Visit on the Web (hosted by [Heroku](https://heroku.com/))

[Iris Prediction](https://immense-coast-7696.herokuapp.com/)

*...when you get there - click "Input Form" to start ...*

## INSTALL

the required python libraries are housed in a standard
requirements.txt file - to install them just use:

```{bash, echo=FALSE}
pip install -r requirements.txt
```

Be sure to add your Domino API Key to your environment (see below)

and then just run:

```{bash, echo=FALSE}
python flask_iris.py
```

## Domino API Key

You'll need to use your own domino inspired api key. First
signup with a free account at [Domino](https://www.dominodatalab.com/)
then sign in and go to your
[Account Settings](https://app.dominodatalab.com/account)
where you will find your own personal API key. Copy it.

To run these commands you'll want to set the environment variable:
DOMINO_API_KEY before they'll work.

```{bash, echo=FALSE}
export DOMINO_API_KEY=<YOUR API KEY>
```

on windows you'll need to use the **set** command

```{bash, echo=FALSE}
set DOMINO_API_KEY=<YOUR API KEY>
```

## Included Files

**Presentation Software**

* deploy-model.Rmd - ioslides presentation
* deploy-model.html - in html format
* image - directory to hold... um... something...
* domino_iris.Rproj - project deployment

**Executables**

* cli.sh - shell script example for making domino connection
* flask_iris.py - python script for running a simple website
* templates/ - directory for housing jinja2 templates
* static/ - static files for flask
* requirements.txt - python library requirements

## Security Updates

* requests == 2.2.20.0
* flask == 0.12.3

## Authors

**Daniel Emaasit** (Ph.D. Student)

Use R for statistical programming in my research to solve Transportation Engineering problems like crashes, congestion e.t.c.

* Github: [https://github.com/Emaasit](https://github.com/Emaasit)
* Email: [daniel.emaasit@gmail.com](mailto:daniel.emaasit@gmail.com)
* Website: [http://www.danielemaasit.com](http://www.danielemaasit.com)

**Steve Wells** (C.T.O, Cumulus)  

Computer Programmer & Data Scientist

* Github: [https://github.com/yxes](https://github.com/yxes)
* Email: [yxes@cpan.org](mailto:yxes@cpan.org)
* Website: [http://www.stephendwells.com/](http://www.stephendwells.com/)
