from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from app import mail
from app.common.file import put_to_file

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    #mail.send(msg)
    Thread(target=send_async_email, args=(current_app, msg)).start()
    if (current_app.config['IS_LOGGING_MAIL']):
        debug_email(subject, sender, recipients, text_body)

def send_password_reset_email(member):
    token = member.get_reset_password_token()
    send_email('[{}] Reset Your Password'.format(current_app.config['FBD_SITE_NAME']),
               sender=current_app.config['FBD_ADMIN_MAIL'],
               recipients=[member.email],
               text_body=render_template('email/reset_password.txt',
                                         member=member, token=token),
               html_body=render_template('email/reset_password.html',
                                         member=member, token=token))

def debug_email(subject, sender, recipients, body):
    data = '\n-----------------------------\n'
    data += 'to: {}\nfrom: {}\nsubject: {}\n'.format(', '.join(recipients), sender, subject)
    data += '---------------\n'
    data += body
    data += '\n-----------------------------\n'
    put_to_file('logs/mail.log', data)
