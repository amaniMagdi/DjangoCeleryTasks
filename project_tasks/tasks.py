#import celery instance
from project.celery import app
from celery import shared_task
import time

#this tasks will run when it called from views.py
@shared_task
def send_mass_emails(recipient):
    print(recipient)
    print("Started to sleep")
    time.sleep(5)
    print("wake up from sleep")
    return 


#task decorator used for scheduled tasks
@app.task
def send_scheduled_emails():
    #scheduled task
    pass
    

