from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from .models import HTMLEMAIL
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home(request):
    
    return render(request,"htmlemail/home.html",{})
        


        



from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse

def send_html_email(request):
    if request.method=='POST':
        subject = 'TEST EMAIL SYSTEM'
        to_email = request.POST.get('email')
        submitted_html = request.POST.get('text').strip()
        from_email = 'kjjose00@gmail.com'
        print("hello world")
    
        text_content = 'This is the plain text version of the email.'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.content_subtype = "html"
        msg.attach_alternative(submitted_html, 'text/html')
        try:
            msg.send()
            
            return HttpResponse('Email sent successfully')
        except Exception as e:
            return HttpResponse(f'An error occurred: {str(e)}')
        
    else:
        return HttpResponse("please submit form")  



            

    





