flask-boilerplate
=================

A flask-app boilerplate WITHOUT blueprints and extra fluff, I'm using this for 
smaller and larger projects where I don't need to use the app-factory pattern 
or split the app up with BluePrints.

This app uses;
* Flask
* Bootstrap 2.3.2
* jQuery 1.10.1
* flask-SQLAlchemy (MySQL)
* flask-mail (With asyncronous sending just for show)
* flask-wtforms
* Logging
* Passlib (py-bcrypt)

Design/Layout decisions;
* Bootstrap Navbar
* Jumbotron on index.html (Style in static/custom.css)
* Footer fixed to bottom of page
* Using netdna.bootstrapcdn.com for bootstrap includes (makes it easy to change version)
* Using ajax.googleapis.com for jquery includes (makes it easy to change version)
