from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from. models import tb



# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message

        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['infoanoop0@gmail.com'])



    return render(request,"index.html",{})

# def tlb(request):
#     # obj = tb.objects.all()
#
#     return render(request,"text.html",{'ob':obj})
#

