from flask import request, redirect, url_for, session, flash
from functools import wraps
from threading import Thread

"""
    Decorate URL's that require authentication with @requires_auth, this will 
    check if 'is_authenticated' is in the session and otherwise redirect the 
    request with a flash-message
"""
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('is_authenticated'):
            flash('You are not authenticated', 'info')
            return redirect( url_for('show_index') )

        return f(*args, **kwargs)

    return decorated

"""
    Decorate methods that should be run in the background (asyncronous). 
    For an example, see the mailer.send_async_mail() method. 
"""
def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper
