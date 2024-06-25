from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail
from myapp.models import Contact


# class HomePageView(TemplateView):
#     template_name = 'index.

def index(request):
    return render(request, 'index.html')


def contact_view(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    subject = request.POST.get('subject')
    message = request.POST.get('message')

    Contact.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)

    subject = "Thank you for contacting us"
    message = 'Hello, ' + request.POST[
        'name'] + '\n\n' + 'I have received your message and will get back to you soon.\n\nBest regards\n Surendrasingh Sodha'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.POST['email'], ]
    send_mail(subject, message, email_from, recipient_list)

    subject1 = 'Contact from Website'
    message1 = 'Hello Surendrasingh, ' + '\n\n' + request.POST['name'] + ' want to contact you.' + '\n\n' + 'Name : ' + \
               request.POST['name'] + '\n' + 'Email : ' + request.POST['email'] + '\n' + 'Subject : ' + request.POST[
                   'subject'] + '\n' + 'Message : ' + request.POST['message']
    recipient_list1 = ['surendradjangotest@gmail.com', ]
    send_mail(subject1, message1, email_from, recipient_list1)

    return redirect('/')
