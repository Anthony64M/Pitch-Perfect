from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**k8ddj6m2l):
    sender_email = 'pitchworld4@gmail.com'
    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**k8ddj6m2l)
    email.html = render_template(template + ".html",**k8ddj6m2l)
    mail.send(email)