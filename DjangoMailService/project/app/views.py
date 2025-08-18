from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(req):
    return render(req, "home.html")

def sendmail(req):

    # For SINGLE MAIL
#     send_mail(
#     "Django Mail Testing",
#     "Message sent Successfully.",
#     "harshalthakre0403@gmail.com",
#     ["harshal22thakre@gmail.com"],
#     fail_silently=False,
# )
    return render(req, "home.html")