# -*- coding: utf-8 -*-

import datetime
from flask.ext.mail import Mail, Message

from webapp import app
from utils import get_client_ip
from decorators import async

mail = Mail(app)

@async
def send_async_email(msg):
    mail.send(msg)

def send_message(subject, message, from_email, to_email):
    dt = datetime.datetime
    msg = Message(subject, 
                    sender=from_email,
                    recipients=[to_email])
    msg.body = message + '\n\nSent at ' + str(dt.now()) + ' from ' + str(get_client_ip()) + '\n'

    send_async_email(msg)
    app.logger.debug('E-mail sent to %s ' % to_email)
    return True
