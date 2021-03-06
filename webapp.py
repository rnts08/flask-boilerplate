#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, session, redirect, url_for, \
                  abort, render_template, flash, send_from_directory, \
                  jsonify

from sqlalchemy.exc import IntegrityError, OperationalError

import logging
from logging import FileHandler, Formatter

from models import db, User
from forms import RegistrationForm
from utils import timestamp, is_email, get_client_ip, hash_password, verify_password, flash_errors
from decorators import requires_auth, jsonp

# Initialize application
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

import mailer

"""
    External/Public Website
"""

@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if request.method == 'GET':
        return render_template('register.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            user = User()
            form.populate_obj(user)
            # overwrite the old password with a bcrypt-hash
            user.password = hash_password(user.password)
            try:
                user.save()
                app.logger.info('New user registered')
                flash('User registered successfully', 'success')
            except IntegrityError as err:
                app.logger.warning('Could not register user: {0}'.format(err))
                flash('User could not be registered, please try again', 'error')
            except OperationalError as err:
                app.logger.warning('MySQL Error: {0!s}'.format(err))
                flash('{0!s}'.format(err))

            return redirect( url_for('show_index') )
        else:
            flash_errors(form)
        return render_template('register.html', form=form)

@app.route('/email', methods=['POST'])
def send_email():
    if is_email(request.form['email']) and len(request.form['subject']) >= 2 and len(request.form['message']) >= 10:
        mailer.send_message(request.form['subject'], request.form['message'], request.form['email'], app.config['COPY_MAIL'])
        flash('Your e-mail was sent succesfully', 'success')
    else:
        flash('Please check the form, I don\'t want junk please.','error')
    return redirect( url_for('show_index') )

@app.route('/login', methods=['POST', 'GET'])
def login():
    """
        This is left as an excersice for you, implement your login however you
        want, but I would probably do something like this:
        try:
            user = db.session.query(User).filter(User.email == request.form['email']).one()
        except sqlalchemy.orm.exc.NoResultFound:
            flash('Invalid username or password', 'error')
            return redirect( url_for('login') )
        
        if verify_password(request.form['password'], user.password):
            session['is_authenticated'] = True
            session['user'] = user
        else:
            flash('Invalid username or password','error')
            return redirect( url_for('login') )
    """
    if request.method == 'GET':
        return redirect( url_for('show_index') )
    else:
        app.logger.debug('User %s logged in' % request.form['email'])
        session['is_authenticated'] = True
        flash('Successfully logged in', 'success')
        return redirect( url_for('show_index') )

@app.route('/logout')
def logout():
    session['is_authenticated'] = False
    session.clear()
    flash(u'Successfully logged out.', 'success')
    return redirect( url_for('show_index') )    

@app.route('/protected')
@requires_auth
def protected_url():
    flash('Authentication successful','success')
    return redirect( url_for('show_index') )

@app.route('/crossdomain_json')
@jsonp
def crossdomain_json():
    data = {'this': 'can', 'be': 'called', 'remotely': 'yeah!'}
    return jsonify(data)

"""
    Static resources
"""

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'images/favicon.ico')

@app.route('/init_db')
def init_db():
    if app.config['DB_CREATED']:
        app.logger.warning('Someone (%s) tried to access init_db' % get_client_ip())
        return redirect( url_for('show_index') )
    else:
        db.create_all()
        app.logger.info('%s created database tables with /init_db' % get_client_ip())
        flash('Database created, please update config.py')
        return redirect( url_for('show_index') )

## 
## passing functions to jinja
##
app.jinja_env.globals.update(timestamp=timestamp)
app.jinja_env.globals.update(client_ip=get_client_ip)

if __name__ == '__main__':
    """
        Setup logging format and files 
    """
    file_handler = FileHandler(app.config['LOG_FILE'])
    file_handler.setLevel(app.config['LOG_LEVEL'])
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    app.run(host=app.config['HOST'], port=app.config['PORT'], 
            debug=app.config['DEBUG'], use_reloader=True)
    app.logger.addHandler(file_handler)
