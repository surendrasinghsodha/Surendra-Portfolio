from django.core.mail import send_mail


def custom_send_mail(subject, message, default_from_mail, to=None, cc=None, bcc=None, is_html=False):
    send_mail(subject, message, default_from_mail, to, cc, bcc, )
    print("Email Sent")
