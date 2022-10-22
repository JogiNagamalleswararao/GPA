import email
from  django.core.mail import send_mail

from django.conf import settings

def forget_pass(username,token):
    sub="your forget password line:"
    msg=f'hi, click the link http://127.0.0.1:8000/index1/{token}/'
    email_from=settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(sub,msg,email_from,recipient_list)
    return True