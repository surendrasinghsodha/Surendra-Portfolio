from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')


def contact_view(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    subjects = request.POST.get('subject')
    messages = request.POST.get('message')

    try:
        subject = "Thank you for contacting us"
        message = 'Hello, ' + name + '\n\n' + ('I have received your message and will get back to you soon.'
                                               '\n\nBest regards\nSurendrasingh Sodha')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, message, email_from, recipient_list)

        subject1 = 'Contact from Website'
        message1 = ('Hello Surendrasingh, ' + '\n\n' + request.POST['name'] + ' want to contact you.' + '\n\n' +
                    'Name : ' + name + '\n' +
                    'Email : ' + email + '\n' +
                    'Phone : ' + phone + '\n' +
                    'Subject : ' + subjects + '\n' +
                    'Message : ' + messages)
        recipient_list1 = ['surendradjangotest@gmail.com', ]
        send_mail(subject1, message1, email_from, recipient_list1)
    except:
        print("Data not Found in database")

    return redirect('/')
