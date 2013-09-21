YetAnotherFlaskBoilerPlate
=================
(Was: Flask-Boilerplate)

A flask-app boilerplate WITHOUT blueprints and extra fluff, I'm using this for 
smaller and larger projects where I don't need to use the app-factory pattern 
or split the app up with BluePrints.

## Special Features
* Send e-mail with flask-mail
* Passing class methods to a SQLAlchemy class (models.py/dbCRUD)
* Crossdomain JSON functionality (decorators.py/jsonp)
* Shooting off threads for blocking methods (decorators.py/async)
* Static robots.txt and favicon.ico routes
* Decorated authentication (decorators.py/requires_auth)
* WTForms usage
* SQLAlchemy usage
* Logging
* bcrypt-hashing/verification of 'passwords'
* And More

## Design/Layout decisions
* Bootstrap Navbar
* Jumbotron on index.html (Style in static/custom.css)
* Footer fixed to bottom of page
* Using netdna.bootstrapcdn.com for bootstrap includes (makes it easy to change version)
* Using ajax.googleapis.com for jquery includes (makes it easy to change version)

## Installation

- git clone https://github.com/rnts08/flask-boilerplate.git myapp
- cd myapp
- (Edit config.py, create database and user in mysql)
- virtualenv .env --no-site-packages
- source .env/bin/activate
- pip install -r /path/to/requirements.txt
- python webapp.py

Done, browse to http://localhost:9000

If you've setup MySQL you can go to http://localhost:9000/init_db and it should
create your table(s) according to models.py. Don't forget to update config.py 
and set DB_CREATED=True. 

## Donate
If you like or use this, feel free to donate to

BTC: 1rntsUZrVkfbNNixDcVoaFwEKeAYff6jb
LTC: LWbNEKnRtqhq3bh2A6AjmeYZJmjk9HbPGi

## License
Because, why not. CDDL-style license, the software is provided as-is, I can't be
held responsible for anything, patent trolls can go and die in a fire and if 
you meet me, you might buy me a beer at your own discretion.

http://opensource.org/licenses/CDDL-1.0

Each plugin and component might have it's own license that applies. 
