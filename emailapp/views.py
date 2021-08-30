from EmailProject2.settings import EMAIL_HOST_USER

from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail


from EmailProject2.settings import EMAIL_HOST_USER



def home(request):
    return HttpResponse("HELLO DJANGO")





# def email_view(request):
    # to = 'akumatha@gmail.com'
    # sub = "GREETINGS GARTITUDE"
    # message = "YOU GOT JOB"

    # email = send_mail(sub,message,EMAIL_HOST_USER,(to)

    # if email:
    #     return HttpResponse("Your email has succes ")
    # else:
    #     return HttpResponse("Not Sended")

#     return render(request,'email/email.html')


def email_view(request):
    if request.method=="POST":
        to = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('messages')

        email = send_mail(sub,msg,EMAIL_HOST_USER,[to])

        if email:
            return HttpResponse("MAIL SEND")
        else:
            return HttpResponse("NOt send")

    return render(request,'email/email.html')
    


