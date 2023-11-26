from django.shortcuts import render
from .tasks import send_mass_emails

def mass_email_view(request):
    recipient = "amani@example.com"
    print("received the request")
    send_mass_emails.delay(recipient)
    print("sent to celery")
    return render(request, "index.html")
