# -*- coding: utf-8 -*-

import datetime
import re
from flask import request
from passlib.hash import bcrypt

def timestamp():
    dt = datetime.date
    return dt.today().strftime('%b %d, %Y')

def is_email(email):
    email_re = re.compile(r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$', re.IGNORECASE)
    if email_re.findall(email):
        return True
    return False

def get_client_ip():
    if 'X-Forwarded-For' in request.headers:
        return request.headers.get('X-Forwarded-For')
    else:
        return request.remote_addr

def hash_password(password):
    return bcrypt.encrypt(password) 

def verify_password(password, hash):
    return bcrypt.verify(password, hash)
