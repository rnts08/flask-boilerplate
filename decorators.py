from flask import request, redirect, url_for, session, flash, Response
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

"""
Make the response a valid jsonp-object for cross-domain remote calls 
from an ajax/jquery frontend. 
"""
def jsonp(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return Response(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function

